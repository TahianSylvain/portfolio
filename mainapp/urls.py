from .views import landing
from django.urls import path 

urlpatterns = [
    path('', landing),
]