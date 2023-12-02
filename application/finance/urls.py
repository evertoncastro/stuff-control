from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r'expenses', views.ExpenseView, 'finance-expenses')


urlpatterns = [
    path('finance/', include(router.urls)),
]

