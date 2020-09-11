from accounts.models import Account
from apple.models import BadApple
from incident.models import Incident


def seedIncident(reported_by: Account, badApple: BadApple, summary: str, details: str) -> Incident:
    return Incident.objects.create(
        reported_by=reported_by,
        apple=badApple,
        summary=summary,
        details=details,
    )
