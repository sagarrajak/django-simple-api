from rest_framework.views import APIView
from rest_framework.response import Response 

class HelloApiView(APIView):
  """ Hello api view"""
  def get(self, request, format=None):
    an_apiview = [
      'sdsdsd sdsdsd'
    ]
    return Response({ 'message': 'some', 'an_apiview': an_apiview })
  