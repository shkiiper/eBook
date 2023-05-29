from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, PageViewSet

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'pages', PageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]