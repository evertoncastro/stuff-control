from django.test import TestCase
from application.finance.expenses import ExpenseManager
from application.common.tests.test_mixins import TestMixins


class ExpenseManagerTestCase(TestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()

    def test_create_expense_from_coupon(self):
        coupon = self.create_coupon(user=self.user, amount=50.5)
        expense = ExpenseManager().create_expense_from_coupon(coupon)
        self.assertEqual(expense.coupon, coupon)
        self.assertEqual(expense.user, coupon.user)
        self.assertEqual(expense.amount, coupon.amount)
        self.assertEqual(expense.title, "Expense")
        self.assertTrue(expense.verified)
        

