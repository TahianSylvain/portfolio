from .views import landing, faqs, download
from django.urls import path 


urlpatterns = [
    path('', landing, name='landing'),
    path('faqs/', faqs, name="faqs"),
    path('download/', download, name="download")
]
