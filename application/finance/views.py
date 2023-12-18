from .models import Expense, Coupon
from rest_framework import viewsets
from rest_framework import pagination
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import ExpenseSerializer, CreateExpenseFromCouponQrcodeSerializer
from .expenses import ExpenseManager
from .coupons import CouponManager


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
    viewsets.ModelViewSet
):
    serializer_class = CreateExpenseFromCouponQrcodeSerializer
    queryset = Expense.objects.all().order_by('-created_at')
    pagination_class = ExpenseResultsSetPagination
    
    @action(detail=False, methods=['post'], url_name='qrcode')
    def qrcode(self, request):
        serializer = CreateExpenseFromCouponQrcodeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        coupon: Coupon = CouponManager().create_from_qrcode(
            request.user, serializer.data["qrcode_data"]
        )
        expense: Expense = ExpenseManager().create_expense_from_coupon(coupon)
        return Response({'id': expense.id}, status=status.HTTP_201_CREATED)