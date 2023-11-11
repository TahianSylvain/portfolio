from django.contrib import admin
from django.urls import path, include
from django.conf import settings, urls
from django.conf.urls.static import static
from django.views.static import serve


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainapp.urls')),
    urls.url(r'^download/(?P<path>.*)$',
             serve, {"document_root": settings.MEDIA_ROOT}
    ),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

