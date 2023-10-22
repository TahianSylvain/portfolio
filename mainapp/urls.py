from .views import landing, about, faqs
from django.urls import path 

urlpatterns = [
    path('', landing, name='landing'),
    path('faqs/', faqs, name="faqs"),
    path('about/', about, name="about"),
]