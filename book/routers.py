from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, PageViewSet, BookDetailView, PageDetailView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'pages', PageViewSet)
router.register(r'book', BookDetailView, basename='book-detail')
router.register(r'book/(?P<book_id>\d+)/page', PageDetailView, basename='page-detail')

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]