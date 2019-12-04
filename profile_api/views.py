from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated
from profile_api import serializers, models, permission

class HelloApiView(APIView):
    """ Hello api view"""
    serializer_class = serializers.HelloSerializers

    def get(self, request, format=None):
        an_apiview = [
            'sdsdsd sdsdsd'
        ]
        return Response({'message': 'some', 'an_apiview': an_apiview})

    def post(self, request):
        """create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """"Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """Handle patch request"""
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """Delete a entry from database """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test Api ViewSet """

    serializer_class = serializers.HelloSerializers;

    def list(self, request):
        """return as hello message"""
        a_viewset = [
            "The need for boilerplate can be reduced through high-level mechanisms such ",
            "business.Columns and other pieces that were distribute"
        ]
        return Response({'message': 'hello', 'a_viewset': a_viewset});

    def create(self, request):
        """Create new Hello message"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

    def retrieve(self, request, pk=None):
        """ Getting a object by it's id """
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        """ Handle updating an object """
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ Handle creating and updating profile """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permission.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", 'email',)


class UserLoginApiViews(ObtainAuthToken):
    """ Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES
 
class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handle creating reading and updating profile feed items """
    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    permission_classes = (
        permission.UpdateOwnStatus,
        IsAuthenticated
    )
        
    def perform_create(self, serializer):
        """set user profile to a logged in user"""
        serializer.save(user_profile=self.request.user)