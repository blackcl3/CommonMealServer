from django.db import models

class FoodItemCategory(models.Model):
    food_item = models.ForeignKey("FoodItem", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
