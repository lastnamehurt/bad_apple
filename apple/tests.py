# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

# Create your tests here.
from accounts.seed import seedAccountUser
from apple.models import BadApple
from apple.services import badAppleService
from apple.usecases import CreateBadApple
from core.usecases import UseCaseManager
from incident.models import Incident
from incident.seed import seedIncident
from incident.services import incidentService
from incident.usecases import CreateIncidentWithNoBadApple
from utils.helpers import reloadObject


class BadAppleAcceptanceTests(TestCase):
    def setUp(self) -> None:
        self.account = seedAccountUser()
        self.badApple = badAppleService.create(
            {
                'first_name': 'Bad',
                'last_name': 'Apple',
                'description': 'Test Create',
            }
        )

    def tearDown(self) -> None:
        BadApple.objects.all().delete()
        Incident.objects.all().delete()

    def testCreateBadApple(self):
        """
        Assumes this Bad Apple does not exist
        """
        self.assertEqual(self.badApple.first_name, 'Bad')
        self.assertEqual(self.badApple.last_name, 'Apple')
        self.assertEqual(self.badApple.description, 'Test Create')

    def testCreateIncidentForExistingBadApple(self):
        summary = 'Test Incident for Existing Bad Apple'
        incident = seedIncident(
            self.account,
            self.badApple,
            summary,
            'Testing'
        )
        self.assertEqual(incident.reported_by, self.account)
        self.assertEqual(incident.apple_id, self.badApple.id)
        self.assertEqual(incident.summary, summary)

    def testCreateIncidentWithNoBadApple(self):
        summary = 'Test Incident for Existing Bad Apple'
        incident = seedIncident(
            self.account,
            None,
            summary,
            'Testing'
        )
        self.assertIsNone(incident.apple)

    def testAddBadAppleToExistingIncident(self):
        summary = 'Test Incident for Existing Bad Apple'
        incident = seedIncident(
            self.account,
            None,
            summary,
            'Testing'
        )
        # Incident has no BadApple
        self.assertEqual(incident.apple, None)

        # add the apple
        incidentService.assignBadAppleToIncident(incident.id, self.badApple.id)
        reloadObject(incident)

        self.assertEqual(incident.apple_id, self.badApple.id)

    def testCopyIncident(self):
        incident = seedIncident(
            self.account,
            None,
            'test summary',
            'Test Copy'
        )
        incidentCopy = incidentService.copyIncident(incident.id)

        self.assertDictEqual(incidentCopy.context(), incident.context())
        self.assertIsNone(incidentCopy.id)

        # now save the object to ensure an id was created
        incidentCopy.save()

        self.assertIsNotNone(incidentCopy.id)
        self.assertEqual(incidentCopy.id, incidentService.getAllObjects().last().id)

    def testCreateBadAppleUseCase(self):
        data = {
            'first_name': 'Yez',
            'last_name': 'Zir',
            'description': 'Usecase test',
        }
        UseCaseManager(CreateBadApple, filters=data).execute()

        newBadApple = badAppleService.getAllObjects().last()

        self.assertEqual(newBadApple.first_name, 'Yez')
        self.assertEqual(newBadApple.last_name, 'Zir')
        self.assertEqual(newBadApple.description, 'Usecase test')

    def testCreateIncidentWithoutBadAppleUseCase(self):
        data = {
            'summary': 'test usecase',
            'details': 'details test',
            'city': 'Seattle',
            'state': 'WA',
            'zipCode': '91108',
            'reported_by_id': 1,
        }
        UseCaseManager(CreateIncidentWithNoBadApple, filters=data).execute()
        newIncident = incidentService.getAllObjects().last()

        self.assertEqual(newIncident.summary, data['summary']),
        self.assertEqual(newIncident.details, data['details']),
        self.assertEqual(newIncident.city, data['city']),
        self.assertEqual(newIncident.state, data['state']),
        self.assertEqual(newIncident.zipCode, data['zipCode']),
