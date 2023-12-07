from django.contrib import admin
from django.urls import path, re_path, include
from .views import catchall
    

urlpatterns = [
    path('admin', admin.site.urls),
    path('api/', include('application.finance.urls')),
    path('api/', include('application.authentication.urls')),
    re_path(r'', catchall),
]
