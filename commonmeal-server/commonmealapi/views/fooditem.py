from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from datetime import date
from commonmealapi.models import FoodItem, User, FoodItemCategory

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
        status = request.query_params.get('status', None)
        location = request.query_params.get('location', None)
        if uid is not None:
            user = User.objects.get(uid=uid)
            food_items = food_items.filter(uid=user.id, status='unavailable')
        if status is not None:
            food_items = food_items.filter(status=status)
        if location is not None: 
            user = User.objects.get(uid=uid)
            food_items = food_items.filter(uid=user, location=location)
        serializer = FoodItemSerializer(food_items, many=True)
        return Response(serializer.data)

    def create(self, request):
        food_item = FoodItem.objects.create(
        uid=User.objects.get(uid=request.data["uid"]),
        name=request.data["name"],
        date=request.data["date"],
        photo_url=request.data["photo_url"],
        status=request.data["status"],
        location=request.data["location"],
        description=request.data["description"]
        )
        serializer = FoodItemSerializer(food_item)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """PUT on food item

        Args:
            request (_type_): _description_
        """
        food_item = FoodItem.objects.get(pk=pk)
        food_item.name = request.data["name"]
        food_item.date = request.data["date"]
        food_item.photo_url = request.data["photo_url"]
        food_item.status = request.data["status"]
        food_item.location = request.data["location"]
        food_item.description = request.data["description"]
        
        food_item.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        
    def destroy(self,request, pk):
        food_item = FoodItem.objects.get(pk=pk)
        food_item.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodItem
        fields = ('id', 'name', 'uid', 'date', 'photo_url', 'status', 'location', 'description', 'food_item_category')
        depth = 2
