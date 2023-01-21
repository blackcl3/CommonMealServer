from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from commonmealapi.models import FoodItem, FoodItemCategory, Category

class FoodItemCategoryViewSet(ViewSet):
    
    def list(self, request):
        food_item_categories = FoodItemCategory.objects.all()
        categories = Category.objects.all()
        food_item = request.query_params.get('food_item', None)
        if food_item is not None:
            food_item_categories = food_item_categories.filter(food_item=food_item)
        serializer = FoodItemCategorySerializer(food_item_categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        food_items = request.data
        for item in food_items:
            food_item = FoodItem.objects.get(id=item['food_item'])
            category = Category.objects.get(id=item['category'])
            food_item_category = FoodItemCategory(
                food_item = food_item,
                category = category)
            food_item_category.save()
        serializer = FoodItemCategorySerializer(food_item_category)
        return Response(serializer.data)
    
class FoodItemCategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItemCategory
        fields = ('id', 'food_item', 'category')
        depth = 2
