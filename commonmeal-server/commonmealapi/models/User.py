from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    uid = models.CharField(max_length=50)
    public_profile = models.BooleanField()
    photo_url = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    neighborhood = models.ForeignKey("Neighborhood", on_delete=models.CASCADE)
