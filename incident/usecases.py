from incident.services import incidentService
from core.usecases import BaseUseCase


class CreateIncidentWithNoBadApple(BaseUseCase):
    serviceMethod = incidentService.createIncidentWithNoBadApple

class CreateIncident(BaseUseCase):
    serviceMethod = incidentService.create
