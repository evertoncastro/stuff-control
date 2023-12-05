from .models import Expense
from .serializers import ExpenseSerializer
from rest_framework import viewsets
from rest_framework import pagination


class ExpenseResultsSetPagination(pagination.PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 20


class ExpenseGenericViewSet(
    viewsets.ModelViewSet
):
    serializer_class = ExpenseSerializer
    queryset = Expense.objects.all().order_by('-created_at')
    pagination_class = ExpenseResultsSetPagination
