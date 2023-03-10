from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from commonmealapi.models import User, Neighborhood

class UserViewSet(ViewSet):
    
    def retrieve(self, request, pk):
        """GET requests for a single user

        Args:
            response -- JSON serialized user
        """
        user = User.objects.get(pk=pk)
        # uid = request.META['HTTP_AUTHORIZATION']
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):
        """GET requests for all users

        Args:
            response -- JSON serialized list of users
        """
        users = User.objects.all()
        uid = request.query_params.get('uid', None)
        if uid is not None:
            users = users.filter(uid=uid)
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk):
        """PUT for user

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        user = User.objects.get(pk=pk)
        uid = request.query_params.get('uid', None)
        if uid is not None:
            user = User.objects.get(uid=uid)
        neighborhood = Neighborhood.objects.get(
            pk=request.data["neighborhood"])
        user.name = request.data["name"]
        user.public_profile = request.data["public_profile"]
        user.photo_url = request.data["photo_url"]
        user.address = request.data["address"]
        user.neighborhood = neighborhood
        user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        """DELETE user

        Args:
            request (_type_): _description_
            pk (_type_): _description_
        """
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'name', 'uid', 'public_profile', 'photo_url', 'address', 'neighborhood')
        depth=1
