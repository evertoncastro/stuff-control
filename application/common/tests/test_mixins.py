from faker import Faker
from application.authentication.models import User

dummy = Faker()

class TestMixins:

    def create_user(self, **kwargs) -> User:
        user = User(
            email=dummy.email(),
            is_active=True
        )
        if kwargs.get("password"):
            user.set_password(kwargs["password"])
        user.save()
        return user