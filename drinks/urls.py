from django.urls import path
from .views import drink_list,drink_detail
from . import views

urlpatterns = [
    path('api/', views.drink_list),
    path('api/<int:id>', views.drink_detail),
]
