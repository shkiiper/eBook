from django.contrib import admin

from book.models import Book, Page

admin.site.register(Book)
admin.site.register(Page)