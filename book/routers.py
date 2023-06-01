from django.urls import include, path
from rest_framework import routers

from .views import BooksViewSet, PageViewSet, BookViewSet

router = routers.DefaultRouter()
router.register(r'books', BooksViewSet)
router.register(r'pages', PageViewSet)
router.register(r'book', BookViewSet, basename='book')
urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]