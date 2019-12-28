
from django.contrib import admin
from django.urls import path,include
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from .routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('auth/token/' , TokenObtainPairView.as_view()),
    path('auth/token/refresh/' , TokenRefreshView.as_view()),
]


