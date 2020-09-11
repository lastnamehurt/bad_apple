from accounts.models import Account
from core.core_repo import BaseRepo


class AccountRepo(BaseRepo):
    model = Account


accountRepo = AccountRepo()
