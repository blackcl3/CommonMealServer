from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=50)
    uid = models.ForeignKey("User", on_delete=models.CASCADE)
    date = models.DateField()
    photo_url = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
