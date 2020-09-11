from apple.services import badAppleService
from core.core_service import BaseService
from incident.repo import incidentRepo


class IncidentService(BaseService):
    repo = incidentRepo

    @classmethod
    def createIncidentWithNoBadApple(cls, filters):
        if filters.get('apple', None):
            filters['apple'] = None
        return cls.create(filters=filters)

    @classmethod
    def createIncident(cls, filters):
        return cls.create(filters=filters)

    @classmethod
    def assignBadAppleToIncident(cls, incidentId, appleId):
        incident = cls.repo.getById(incidentId)
        badApple = badAppleService.get(appleId)
        incident.apple = badApple
        incident.save()
        return incident

    @classmethod
    def getContext(cls, incidentId):
        incident = cls.repo.getById(incidentId)
        data = {
            'date': incident.date,
            'summary': incident.summary,
            'details': incident.details,
            'city': incident.city,
            'state': incident.state,
            'zipCode': incident.zipCode,
            'reported_by': incident.reported_by,
            'apple': incident.apple,
        }
        return data

    @classmethod
    def copyIncident(cls, incidentId):
        incidentContext = cls.getContext(incidentId)
        return cls.prepare(incidentContext)


incidentService = IncidentService()
