from faker import Faker
from application.authentication.models import User
from application.finance.models import Expense, Coupon

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
    
    def create_expense(self, user, **kwargs) -> Expense:
        expense = Expense(
            user=user,
            title=kwargs.get('title') if kwargs.get('title') else 'My expense',
            amount=kwargs.get('amount') if kwargs.get('amount') else 100
        )
        expense.save()
        return expense
    
    def create_coupon(self, user, **kwargs) -> Coupon:
        amount = kwargs.get("amount") if kwargs.get("amount") else 100
        coupon = Coupon(
            user=user,
            amount=amount,
            raw_data="test",
            extracted_data={
                "amount": amount,
                "issuer": kwargs.get("issuer")
            }
        )
        coupon.save()
        return coupon