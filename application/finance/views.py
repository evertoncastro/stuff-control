from .models import Expense
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ExpenseSerializer, CreateExpenseFromCouponQrcodeSerializer


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
    filterset_fields = ["title"]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)
    

class ExpenseFromCouponGenericViewSet(
    viewsets.ViewSet
):
    @action(detail=False, methods=['post'], url_name='qrcode')
    def qrcode(self, request):
        serializer = CreateExpenseFromCouponQrcodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'status': 'ok'})