from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'expenses', views.ExpenseGenericViewSet, basename='finance-expenses')
router.register(r'expenses/coupon', views.ExpenseFromCouponGenericViewSet, basename='finance-expenses-from-coupon')


urlpatterns = [
    path('finance/', include(router.urls)),
]

