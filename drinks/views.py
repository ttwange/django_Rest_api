from django.http import JsonResponse
from .models import Drink 
from .serializers import DrinkSerializer

# Create your views here.
def drink_list(request):
  #fet all the drinks 
  #serialize them
  #return json