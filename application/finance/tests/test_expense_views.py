import os
from rest_framework.test import APITestCase
from application.common.tests.test_mixins import TestMixins
from django.urls import reverse
from application.finance.models import Expense
from application.finance.serializers import ExpenseSerializer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'application.settings')


class CreateExpenseTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()
        self.client.force_authenticate(self.user)

    def test_create_expense(self):
        url = reverse('finance-expenses-list')
        data = dict(title="My expense", value=100.56)
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        expense: Expense = Expense.objects.get(id=response.json()['id'])
        ser = ExpenseSerializer(expense, many=False)
        self.assertEqual(response.json(), ser.data)


class ListExpenseTestCase(APITestCase, TestMixins):

    def setUp(self) -> None:
        self.user = self.create_user()
        self.client.force_authenticate(self.user)
        self.expense1 = self.create_expense(title="Expense 1")
        self.expense2 = self.create_expense(title="Expense 2")
        self.expense3 = self.create_expense(title="Expense 3")

    def test_list_expense(self):
        url = reverse('finance-expenses-list')
        response = self.client.get(url, format='json')
        query_expense = Expense.objects.all().order_by('-created_at')
        serializer = ExpenseSerializer(query_expense, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), dict(
            count=len(query_expense),
            next=None,
            previous=None,
            results=serializer.data
        ))