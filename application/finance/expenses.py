from application.finance.models import Expense, Coupon
from application.common.services.brasilapi import BrasilAPI


class ExpenseManager:

    def create_expense_from_coupon(self, coupon: Coupon):
        title = "Expense"
        issuer: str = coupon.extracted_data.get("issuer")
        try:
            if issuer:
                title = BrasilAPI().get_company_data(company_id=issuer)["company_name"]
        except Exception:
            ...

        return Expense.objects.create(
            user=coupon.user,
            title=title,
            amount=coupon.amount,
            verified=True,
            coupon=coupon
        )