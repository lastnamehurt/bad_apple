from core.core_repo import BaseRepo
from incident.models import Incident


class IncidentRepo(BaseRepo):
    model = Incident


incidentRepo = IncidentRepo()
