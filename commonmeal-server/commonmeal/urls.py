from django.contrib import admin
from django.urls import path
from commonmealapi.views import register_user, check_user

urlpatterns = [
    path('register', register_user),
    path('checkuser', check_user),
    path('admin/', admin.site.urls),
]
