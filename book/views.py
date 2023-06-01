from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ViewSet

from .models import Book, Page
from .serializers import BookSerializer, PageSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [AllowAny]


class BookViewSet(ViewSet):
    permission_classes = [AllowAny]
    def retrieve(self, request, pk=None):
        try:
            book = Book.objects.get(id=pk)
            pages = Page.objects.filter(book=book)
            serializer = BookSerializer(book)
            data = serializer.data
            data['pages'] = [{'id': page.id, 'chapter': page.chapter, 'content': page.content, 'book': page.book} for page in pages]
            return Response(data)
        except Book.DoesNotExist:
            return Response(
                {"error": "Book does not exist"},
                status=status.HTTP_404_NOT_FOUND
            )