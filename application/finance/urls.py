from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.SimpleRouter()
router.register(r'expenses', views.ExpenseGenericViewSet, basename='finance-expenses')


urlpatterns = [
    path('finance/', include(router.urls)),
]

