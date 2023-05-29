from rest_framework import viewsets
from book.permissions import IsAuthorOrReadOnly, IsAuthorOrReadOnlyForBookPages
from .models import Book, Page
from .serializers import BookSerializer, PageSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthorOrReadOnly]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [IsAuthorOrReadOnlyForBookPages]
