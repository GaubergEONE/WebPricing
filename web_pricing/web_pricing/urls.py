from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('api/', include('ya_disk.urls')),
    path("admin/", admin.site.urls),
    path("__debug__/", include("debug_toolbar.urls")),
]
