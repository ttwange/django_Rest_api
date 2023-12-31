# todo/todo/urls.py : Main urls.py
from django.contrib import admin
from django.urls import path, include
from todo_api import urls as todo_urls
from drinks import urls as drink_urls
from RandomApi import urls as Ran_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('todos/', include(todo_urls)),
    path('drinks/',include(drink_urls)),
    path('RandomApi/', include(Ran_urls))
]