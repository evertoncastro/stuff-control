from django.test import TestCase
from unittest.mock import patch
from application.finance.expenses import ExpenseManager
from application.common.tests.test_mixins import TestMixins


class ExpenseManagerTestCase(TestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()

    @patch("application.finance.expenses.BrasilAPI.get_company_data")
    def test_create_expense_from_coupon(self, mock_company_data):
        mock_company_data.return_value = dict(company_name="Acme S.A.")
        coupon = self.create_coupon(user=self.user, amount=50.5, issuer="some_issuer")
        expense = ExpenseManager().create_expense_from_coupon(coupon)
        self.assertEqual(expense.coupon, coupon)
        self.assertEqual(expense.user, coupon.user)
        self.assertEqual(expense.amount, coupon.amount)
        self.assertEqual(expense.title, "Acme S.A.")
        self.assertTrue(expense.verified)

    @patch("application.finance.expenses.BrasilAPI.get_company_data")
    def test_create_expense_from_coupon_with_error_on_company_data(self, mock_company_data):
        mock_company_data.side_effect = Exception("Some error")
        coupon = self.create_coupon(user=self.user, amount=50.5, issuer="some_issuer")
        expense = ExpenseManager().create_expense_from_coupon(coupon)
        self.assertEqual(expense.coupon, coupon)
        self.assertEqual(expense.user, coupon.user)
        self.assertEqual(expense.amount, coupon.amount)
        self.assertEqual(expense.title, "Expense")
        self.assertTrue(expense.verified)
        

