from .views import landing, download
from django.urls import path 
from django.conf.urls import i18n

urlpatterns = [
    path('', landing, name='landing'),
    path('download/', download, name="download")
]
