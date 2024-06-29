from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
# from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles import models
from profiles import serializers
from profiles import permissions

class HelloAPIView(APIView):
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        messages = [
            'Uses http methods as function(get, post, patch, put, delete)',
            'Similar to a traditional django view',
            'Gives you more control over you application logic',
            'mapped manually to urls'
        ]
        return Response({"result": messages})

    def post(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"result": message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk=None):
        return Response({"result": "PUT"})
    
    def patch(self, request, pk=None):
        return Response({"result": "PATCH"})
    
    def delete(self, request, pk=None):
        return Response({"result": "DELETE"})
    

class HelloViewset(viewsets.ViewSet):
    serializer_class = serializers.HelloSerializer

    def list(self, request):
        messages = [
            'Uses actions (list, create, retrieve, update, destroy, partial_update)',
            'Automatically maps to urls using Routers',
            'Provides more functionality with less code'
        ]
        return Response({"result": messages})
    
    def create(self, request):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            name = serializers.validated_data.get('name')
            message = f"Hello {name}"
            return Response({"result": message})
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def retrieve(self, request, pk=None):
        return Response({"result": "Retrieve"})
    
    def update(self, request, pk=None):
        return Response({"result": "Update"})
    
    def partial_update(self, request, pk=None):
        return Response({"result": "Partial update"})
    
    def destroy(self, request, pk=None):
        return Response({"result": "Destroy"})
    

class UserProfileViewset(mixins.CreateModelMixin, 
                   mixins.RetrieveModelMixin, 
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   viewsets.GenericViewSet):
    serializer_class = serializers.UserProfileSeriazlizer
    queryset = models.UserProfile.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnProfile]
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'email']


# class UserLoginAPIView(ObtainAuthToken):
#     renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ProfileFeedViewset(viewsets.ModelViewSet):
    queryset = models.ProfileFeed.objects.all()
    serializer_class = serializers.ProfileFeedSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.UpdateOwnStatus, IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user_profile=self.request.user)