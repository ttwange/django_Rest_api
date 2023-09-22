from django.urls import path
from drinks import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('api/', views.drink_list),
    path('api/<int:id>', views.drink_detail),
]
urlpatterns = format_suffix_patterns(urlpatterns)