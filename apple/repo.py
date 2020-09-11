from apple.models import BadApple
from core.core_repo import BaseRepo


class BadAppleRepo(BaseRepo):
    model = BadApple


badAppleRepo = BadAppleRepo()
