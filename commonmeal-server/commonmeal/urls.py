from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from commonmealapi.views import register_user, check_user, UserViewSet, NeighborhoodViewSet, FoodItemViewSet, CategoryViewSet, FoodItemCategoryViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, 'user')
router.register(r'neighborhoods', NeighborhoodViewSet, 'neighborhood')
router.register(r'food', FoodItemViewSet, 'foodItem')
router.register(r'categories', CategoryViewSet, 'category')
router.register(r'fooditemcategories', FoodItemCategoryViewSet, 'fooditemcategories')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
