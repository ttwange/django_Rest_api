from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import HelloSerializer


class HelloView(APIView):
  def get(self, request):
    serializer = HelloSerializer()
    return Response(serializer.data)