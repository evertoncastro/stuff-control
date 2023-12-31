from django.db import models
from application.common.models import BaseModel
from application.authentication.models import User
from application.finance.enum import CouponType


class Coupon(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = models.CharField(max_length=20, choices=CouponType.choices(), default=CouponType.UNKNOWN)
    raw_data = models.TextField(null=True, blank=True)
    extracted_data = models.JSONField(null=True, blank=True)
    amount = models.FloatField(null=True)

class Expense(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField(default=0.0)
    verified = models.BooleanField(default=False)
    coupon = models.ForeignKey(Coupon, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return f"{self.title} | {self.amount}"


