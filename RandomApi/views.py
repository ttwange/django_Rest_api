from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_list_or_404

class Random(APIView):
  def get(self, requests, format = None):
    return Response({"message": "I made it"})

  def post(self, requests, format = None):
    data = requests.data
    print(f"data received : {data}")
    return Response({
      "Response":200,
      "Message":data
    })