import os
from rest_framework.test import APITestCase
from application.common.tests.test_mixins import TestMixins
from django.urls import reverse
from application.finance.models import Expense
from application.finance.serializers import ExpenseSerializer
from rest_framework.response import Response

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')


class CreateExpenseTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()
        self.client.force_authenticate(self.user)

    def test_create_expense(self):
        url = reverse('finance-expenses-list')
        data = dict(title="My expense", amount=100.56)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        expense: Expense = Expense.objects.get(id=response.json()['id'])
        ser = ExpenseSerializer(expense, many=False)
        self.assertEqual(response.data, ser.data)


class ListExpenseTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.maxDiff = None
        self.user = self.create_user()
        self.client.force_authenticate(self.user)
        self.expense1 = self.create_expense(self.user, title="Expense 1")
        self.expense2 = self.create_expense(self.user, title="Expense 2")
        self.expense3 = self.create_expense(self.user, title="Expense 3")

    def test_list_expense(self):
        url = reverse('finance-expenses-list')
        response = self.client.get(url, format='json')
        query_expense = Expense.objects.all().order_by('-created_at')
        serializer = ExpenseSerializer(query_expense, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, dict(
            count=len(query_expense),
            next=None,
            previous=None,
            results=serializer.data
        ))

    def test_list_expense_filters_authenticated_user(self):
        other_user = self.create_user()
        self.create_expense(other_user, title="Expense 1")
        self.client.force_authenticate(other_user)

        url = reverse('finance-expenses-list')
        response = self.client.get(url, format='json')
        query_expense = Expense.objects.filter(user=other_user).order_by('-created_at')
        serializer = ExpenseSerializer(query_expense, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, dict(
            count=1,
            next=None,
            previous=None,
            results=serializer.data
        ))

    def test_list_expense_filter_by_title(self):
        url = reverse('finance-expenses-list')
        response = self.client.get(f"{url}?title=Expense 1", format='json')
        query_expense = Expense.objects.filter(user=self.user, title="Expense 1").order_by('-created_at')
        
        serializer = ExpenseSerializer(query_expense, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, dict(
            count=1,
            next=None,
            previous=None,
            results=serializer.data
        ))


class CreateExpenseCouponTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.maxDiff = None
        self.user = self.create_user()
        self.client.force_authenticate(self.user)

    def test_create_without_qrcode_data(self):
        url = reverse('finance-expenses-from-coupon-qrcode')
        data = dict()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {
            'qrcode_data': ['This field is required.']
        })

    def test_create_expense_from_qrcode_successfully(self):
        qrcode = """
        35231210583267000102590004834862957671522157|
        20231209214110|192.34|37893719800|
        WZynT8xRLs2Q8RsU2ncqS4oXFMvZUD3SOeOoelEfr7/
        ntY6lZL6eHbRmLDIECU6cuLNyR6APWTBcklxNvVsB+aqCh9bPlWCpEsQQBbepj23rETZ0jL805+
        aqfsWVfZ42itQxu30SUmeqp0s8q7PXdnFkgo7s29gmRaWba3Y2Y/
        hmLyq1foX6NV7wdb45BNERUtTfZfobhMFD2cTmtp2aOoY2lgfEFOsIbwZSrFam+C6bfOq/
        ffGBRx99EtgBWYGNAVm1kEgJ+c0eZgM0VwaUCvyASvHjoDp8p9KBePJh4HLYAZAje+oNB2G2zPun8Ch8CaZicF/
        9qouZfw7fzhXbCA==
        """
        url = reverse('finance-expenses-from-coupon-qrcode')
        data = dict(qrcode_data=qrcode)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)