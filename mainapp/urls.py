from .views import landing, download
from django.urls import path 
from django.conf.urls import i18n

urlpatterns = [
    # i18n.patterns(
    #     'fr', 
    #     path("", )
    # ),
    path('', landing, name='landing'),
    path('download/', download, name="download")
]
