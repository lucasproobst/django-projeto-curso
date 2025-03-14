from django.urls import path, include
from recipes.views import home

urlpatterns = [
    path('', home),
    path('', include('recipes.urls')),
]
