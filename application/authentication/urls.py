from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views


urlpatterns = [
    path('authentication/token', TokenObtainPairView.as_view(), name='authentication-token'),
    path('authentication/token/refresh', TokenRefreshView.as_view(), name ='authentication-token-refresh'),
    path('authentication/logout', views.LogoutView.as_view(), name ='authentication-logout')
]