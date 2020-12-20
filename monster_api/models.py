from django.db import models

# Create your models here.

class Monster(models.Model):
    name = models.CharField(max_length=255)
    height = models.FloatField()
    description = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)