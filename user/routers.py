from django.urls import path
from rest_framework import routers
from .views import TokenObtainPairView
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    # ... другие URL-шаблоны вашего приложения ...
    path('api/token/', TokenObtainPairView, name='api-token'),  # URL для получения токена аутентификации

]

urlpatterns += router.urls
