from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import  status

from profile_api import serializers


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
