from django.urls import path
from drinks import views

urlpatterns = [
    path('api/', views.drink_list),
    path('api/<int:id>', views.drink_detail),
]
