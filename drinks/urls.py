from django.urls import path
from .views import drink_list
from . import views

urlpatterns = [
    path('', views.drink_list),
    path('/<int:id>', views.drink_list),
]