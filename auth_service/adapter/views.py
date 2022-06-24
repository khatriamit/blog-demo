from auth_service.domain import models
from auth_service.domain import commands
from auth_service.adapter import repository


def register_user(cmd: commands.RegisterUser):
    models.user_factory(**cmd.dict())
    repository_ = repository.UserSQLRepository()
    repository_.register_user(**cmd.dict())
