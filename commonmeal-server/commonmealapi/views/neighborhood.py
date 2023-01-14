from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.decorators import action
from commonmealapi.models import Neighborhood

class NeighborhoodViewSet(ViewSet):
    
    def retrieve(self, request, pk):
        """GET request for a single neighborhood

        Args:
            response -- JSON serialized neighborhood
        """
        neighborhood = Neighborhood.objects.get(pk=pk)
        
        serializer = NeighborhoodSerializer(neighborhood)
        return Response(serializer.data)
    
    def list(self, request):
        """GET request for all neighborhoods

        Args:
            response -- JSON serialized list of neighborhoods
        """

        neighborhoods = Neighborhood.objects.all()
        
        serializer = NeighborhoodSerializer(neighborhoods, many=True)
        return Response(serializer.data)
    
class NeighborhoodSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Neighborhood
        fields = ('id', 'name')
