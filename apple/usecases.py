from apple.services import badAppleService
from core.usecases import BaseUseCase


class CreateBadApple(BaseUseCase):
    serviceMethod = badAppleService.create
