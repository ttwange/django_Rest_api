from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Todo
from .serializers import TodoSerializer

class TodoListApiView(APIView):
  """ Add permission to check if user us authentication"""
  permission_classes = [permissions.IsAuthenticated]

  # 1. List all
  def get (self , request, **args, **kwargs ):
    """ List of all the todo items for given requested user"""
    todos = Todo.objects.filter(user = request.user.id )
    serializer = TodoSerializer(todos,many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
  

  # 2 Create
  def post(self, request,**args, **kwargs):
    """ Create the todo with given todo data"""
    
    data = {
      'title':request.POST['title'],
      'description':request.POST["description"],
      'completed' : False,
      'created_at':datetime.now(),
      'updated_at': datetime.now()

    }

    serializer =  TodoSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)