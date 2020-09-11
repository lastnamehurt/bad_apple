import names
from django.contrib.auth.models import User

from accounts.models import Account


def seedUser():
    return User.objects.create_user(
        names.get_first_name(),
        "{}@example.com".format(names.get_last_name()),
        'test',
    )

def seedAccountUser():
    return Account.objects.create(
        user=seedUser(),
        location='VA'
    )