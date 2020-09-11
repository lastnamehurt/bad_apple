from typing import List

import names

from accounts.models import Account
from accounts.seed import seedAccountUser
from accounts.services import accountService
from incident.seed import seedIncident
from apple.services import badAppleService


def seedBadApple(apples_count: int = 1) -> List[badAppleService.repo.model or None]:
    if apples_count < 2:
        return badAppleService.create(
            {
                'first_name': 'test',
                'last_name': 'user',
            }
        )

    bad_apples = [None] * apples_count
    for i in range(apples_count):
        first_name, last_name = names.get_full_name().split(' ')
        apple = badAppleService.create(
            {
                'first_name': first_name,
                'last_name': last_name,
            }
        )
        bad_apples[i] = apple
    return bad_apples


def seedBadAppleWithIncident(apples_count: int = 1):
    bad_apples = [None] * apples_count
    reportedBy = seedAccountUser()
    import pdb;pdb.set_trace()
    for i in range(apples_count):
        apple = seedBadApple()
        bad_apples[i] = apple
        seedIncident(reportedBy, apple, 'testing', 'detail for testing')
    return bad_apples
