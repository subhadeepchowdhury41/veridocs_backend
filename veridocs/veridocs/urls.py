from unicodedata import name
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('token', TokenObtainPairView.as_view(), name='token-pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='refresh-token')
]
