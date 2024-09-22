from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('notices/',include('notice.urls')),
    path('',include('main.urls')),
    path('info/',include('info.urls')),
]
