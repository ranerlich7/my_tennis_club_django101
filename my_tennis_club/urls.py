
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('members.urls')),
    path('courts/', include('courts.urls')),
    path('admin/', admin.site.urls),
]
