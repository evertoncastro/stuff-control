from application.finance.models import Expense, Coupon



class ExpenseManager:

    def create_expense_from_coupon(self, coupon: Coupon):
        return Expense.objects.create(
            user=coupon.user,
            title="Expense",
            amount=0,
            verified=True,
            coupon=coupon
        )