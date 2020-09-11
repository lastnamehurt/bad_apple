from apple.repo import badAppleRepo
from core.core_service import BaseService


class BadAppleService(BaseService):
    repo = badAppleRepo

    @classmethod
    def getIncidents(cls, badAppleId):
        return cls.repo.getById(badAppleId).incidents

badAppleService = BadAppleService()
