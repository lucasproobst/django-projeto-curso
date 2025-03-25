from django.urls import path, include
from recipes.views import home
from django.contrib import admin

urlpatterns = [
    path('', home),
    path('', include('recipes.urls')),
     path('admin/', admin.site.urls),
]
