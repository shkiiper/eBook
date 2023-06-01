from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Book, Page
from .serializers import BookSerializer, PageSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]


class PageViewSet(viewsets.ModelViewSet):
    queryset = Page.objects.all()
    serializer_class = PageSerializer
    permission_classes = [AllowAny]


class BookDetailView:
    def get(self, request, book_id):
        book = get_object_or_404(Book, pk=book_id)
        pages = Page.objects.filter(book=book).values()

        return JsonResponse({'book': book.__dict__, 'pages': list(pages)})


class PageDetailView:
    def get(self, request, book_id, page_id):
        book = get_object_or_404(Book, pk=book_id)
        page = get_object_or_404(Page, pk=page_id, book=book)

        return JsonResponse({'book': book.__dict__, 'page': page.__dict__})
