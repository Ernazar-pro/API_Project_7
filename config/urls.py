from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from config.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]

urlpatterns += [re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT,}),]