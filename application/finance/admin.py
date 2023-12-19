from django.contrib import admin
from application.finance.models import Expense, Coupon

admin.site.register(Expense)
admin.site.register(Coupon)

