from django.urls import include, path
from rest_framework import routers
from .views import CelebrityViewSet

router = routers.DefaultRouter()
router.register(r'celebrities', CelebrityViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
