from django.db import models

# Create your models here.
class Url(models.Model):
    id = models.CharField(max_length=10, primary_key=True)
    source = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)