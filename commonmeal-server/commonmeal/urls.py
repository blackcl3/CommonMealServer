from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from commonmealapi.views import register_user, check_user, UserViewSet, NeighborhoodViewSet, FoodItemViewSet

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserViewSet, 'user')
router.register(r'neighborhoods', NeighborhoodViewSet, 'neighborhood')
router.register(r'food', FoodItemViewSet, 'foodItem')

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
