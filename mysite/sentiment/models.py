from django.db import models

class File(models.Model):
    session_key = models.CharField(max_length=100, unique=True)
    name = models.CharField(max_length=30)
