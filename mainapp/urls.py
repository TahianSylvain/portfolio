from .views import landing, download, bpmn_modeler
from django.urls import path 
from django.conf.urls import i18n

urlpatterns = [
    path('', landing, name='landing'),
    path('modeler', bpmn_modeler),
    path('download/', download, name="download")
]
