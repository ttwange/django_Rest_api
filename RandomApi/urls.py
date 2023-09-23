from django.urls import path
from .views import Random
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('hello/',Random.as_view(),name='hello'),
]
