from django.db import models

class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    