from django.urls import include, path
from rest_framework import routers
from .views import BookViewSet, PageViewSet, BookDetailView, PageDetailView

router = routers.DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'pages', PageViewSet)
path('book/<int:book_id>/', BookDetailView.as_view(), name='book_detail'),
path('book/<int:book_id>/page/<int:page_id>/', PageDetailView.as_view(), name='page_detail'),

urlpatterns = router.urls

urlpatterns = [
    path('', include(router.urls)),
]