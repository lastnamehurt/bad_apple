from accounts.repo import accountRepo
from core.core_service import BaseService


class AccountService(BaseService):
    repo = accountRepo


accountService = AccountService()