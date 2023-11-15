from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
from django.conf import settings, urls
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext_lazy as _


urlpatterns = i18n_patterns(
    path(_('admin/'), admin.site.urls),
    path('', include('mainapp.urls')),
    re_path(r'^download/(?P<path>.*)$',
        serve, {"document_root": settings.MEDIA_ROOT}
    ),
)

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT)
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)

