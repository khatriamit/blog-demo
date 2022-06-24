from app import models as orm
from django.db import transaction


class UserSQLRepository:
    def __init__(self) -> None:
        pass

    def register_user(self, first_name, last_name, email, username, password):
        with transaction.atomic():
            user = orm.User.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
            )
            user.set_password(password)
            user.save()
            return user
