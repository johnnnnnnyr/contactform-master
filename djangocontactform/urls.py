from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static

from contact.views import index

from django.views.static import serve
from django.urls import include, path


urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
]
