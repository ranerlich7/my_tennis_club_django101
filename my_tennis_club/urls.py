
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('courts/', include('courts.urls')),
    path('members/', include('members.urls')),
    path('admin/', admin.site.urls),
]
