from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import UserViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, basename='users')

urlpatterns = [
    # ... другие URL-шаблоны вашего приложения ...
    path('api/token/', obtain_auth_token, name='api-token'),  # URL для получения токена аутентификации
]

urlpatterns += router.urls
