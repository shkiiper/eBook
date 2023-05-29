from django.db import models


class Celebrity(models.Model):
    name = models.CharField(max_length=255)
    text = models.TextField()
