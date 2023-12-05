from faker import Faker
from application.authentication.models import User
from application.finance.models import Expense

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
    
    def create_expense(self, **kwargs) -> Expense:
        expense = Expense(
            title=kwargs.get('title') if kwargs.get('title') else 'My expense',
            value=kwargs.get('value') if kwargs.get('value') else 100
        )
        expense.save()
        return expense