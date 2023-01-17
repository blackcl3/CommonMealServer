from django.db import models

class FoodItemCategory(models.Model):
    food_item = models.ForeignKey("FoodItem", related_name="food_item_category", on_delete=models.CASCADE)
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
