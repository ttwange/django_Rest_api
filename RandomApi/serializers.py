from rest_framework import serializers

class HelloSerializer(serializers.Serializer):
  """Serializes a name field for testing our APIView."""
  message = serializers.CharField(default="Hello Thon!!")