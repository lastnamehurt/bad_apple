# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from unittest.mock import MagicMock
from unittest.mock import Mock
from unittest.mock import patch

from django.test import TestCase

# Create your tests here.
from accounts.seed import seedAccountUser
from apple.models import BadApple
from apple.seed import seedBadApple
from apple.services import badAppleService
from incident.models import Incident
from incident.seed import seedIncident
from incident.services import incidentService
from utils.helpers import reloadObject


class IncidentServiceTests(TestCase):
    def setUp(self) -> None:
        self.badApple = badAppleService.create(
            {
                'first_name': 'Bad',
                'last_name': 'Apple',
                'description': 'Test Create',
            }
        )
        self.incident = seedIncident(
            seedAccountUser(),
            self.badApple,
            "Incident Service Testing",
            "seeding incident"
        )

    data = {
        'date': None,
        'summary': 'Testing',
        'details': 'Incident Tests',
        'city': 'Seattle',
        'state': 'WA',
        'zipCode': '94118',
        'reported_by_id': 1,
        'apple': None,
    }

    @patch('core.core_repo.BaseRepo.create')
    def testCreateIncidentWithoutBadApple(self, mock_create):
        incidentService.createIncidentWithNoBadApple(self.data)
        mock_create.assert_called_with(self.data)

    @patch('core.core_repo.BaseRepo.create')
    def testCreateIncidentWithBadApple(self, mock_create):
        self.data['apple'] = badAppleService.getAllObjects().last()
        incidentService.createIncident(self.data)
        mock_create.assert_called_with(self.data)

    @patch('core.core_repo.BaseRepo.create')
    def testCreateIncidentWithoutBadAppleWithApplePassedIn(self, mock_create):
        self.data['apple'] = badAppleService.getAllObjects().last()
        self.assertIsNotNone(self.data['apple'])

        incidentService.createIncidentWithNoBadApple(self.data)
        mock_create.assert_called_with(self.data)
        self.assertIsNone(self.data['apple'])

    @patch('core.core_repo.BaseRepo.getById', return_value=Mock(spec=Incident))
    @patch('core.core_service.BaseService.get', return_value=Mock(spec=BadApple))
    def testAssignBadAppleToIncident(self, mock_get_bad_apple, mock_get_incident):
        incident = incidentService.assignBadAppleToIncident(1, 1)
        mock_get_bad_apple.assert_called_with(1)
        mock_get_incident.assert_called_with(1)
        self.assertTrue(incident.apple._spec_class, self.badApple.__class__)

    @patch('incident.services.IncidentService.getContext')
    def testCopyIncident(self, mock_get_context):
        mock_get_context.return_value = self.data
        new_incident = incidentService.copyIncident(self.incident.id)

        mock_get_context.assert_called_with(self.incident.id)
        self.assertTrue(type(new_incident) == Incident)
