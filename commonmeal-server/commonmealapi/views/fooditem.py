from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from commonmealapi.models import FoodItem, User

class FoodItemViewSet(ViewSet):
    
    def retrieve(self, request, pk):
        """GET request for a single food item

        Args:
            response -- JSON serialized food item
        """
        food_item = FoodItem.objects.get(pk=pk)
        
        serializer = FoodItemSerializer(food_item)
        return Response(serializer.data)
    
    def list(self, request):
        """GET requests for all food items

        Args:
            response --JSON serialized list of food items
        """
        food_items = FoodItem.objects.all()
        user = User.objects.all()
        uid = request.query_params.get('uid', None)
        if uid is not None:
            user = User.objects.get(uid=uid)
            food_items = food_items.filter(uid=user.id)
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)

class FoodItemSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'uid', 'date', 'photo_url', 'status', 'location', 'description')
        depth = 1
