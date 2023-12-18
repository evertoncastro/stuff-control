from rest_framework import serializers
from .models import Expense


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = ('id', 'user', 'title', 'amount', 'verified', 'created_at')
        read_only_fields = ('user',)


class CreateExpenseFromCouponQrcodeSerializer(serializers.Serializer):
    qrcode_data = serializers.CharField(required=True)
