from django.db import models

from user.models import User


class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Page(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter = models.CharField(max_length=255)
    content = models.TextField()
