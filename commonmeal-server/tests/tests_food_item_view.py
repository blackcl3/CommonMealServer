from rest_framework import status
from rest_framework.test import APITestCase
from commonmealapi.models import FoodItem, FoodItemCategory, User
from commonmealapi.views.fooditem import FoodItemSerializer, FoodItemCategorySerializer, CategorySerializer

class FoodTests(APITestCase):
    
    fixtures = ['users', 'categories', 'fooditemcategories', 'fooditems', 'neighborhoods']
    
    def setUp(self):
        
        self.user = User.objects.first()
        uid = User.objects.get(uid=self.user.uid)
        self.client.credentials(HTTP_AUTHORIZATION=f"{uid}")

    def test_create_food_item(self):
        """Create Food Item Test"""
        
        url = "/food"
        
        food = {
            "name": "croissant", 
            "uid": "b7jk3WcOXmbb7jJ15MO9SZMYH2E2",
            "description": "typical french pastry",
            "photo_url": "https://static01.nyt.com/images/2023/01/25/multimedia/20Komolafe1-gptj/20Komolafe1-gptj-superJumbo.jpg?quality=75&auto=webp",
            "status": "available",
            "location": "freezer",
            "date": "2023-01-23", 
            "category": []
        }
        
        response = self.client.post(url, food, format='json')
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        new_food_item = FoodItem.objects.last()
        
        expected = FoodItemSerializer(new_food_item)
        
        self.assertEqual(expected.data, response.data)

    def test_get_food_item(self):
        """Get Food Item Test"""
        food_item = FoodItem.objects.first()
        food_item_categories = FoodItemCategory.objects.all()
        food_item_categories = food_item_categories.filter(food_item=food_item)
        
        url = f'/food/{food_item.id}'
        
        response = self.client.get(url)
        
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        
        expected = FoodItemSerializer(food_item)
        print(expected.data)
        print(response.data)
        self.assertEqual(expected.data, response.data)        
        