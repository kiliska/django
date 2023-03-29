from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('django.contrib.flatpages.urls')),
    path('contact/', include('django.contrib.flatpages.urls')),
    path('test', include('django.contrib.flatpages.urls')),
    path('testcurse', include('django.contrib.flatpages.urls')),
    path('test2', include('django.contrib.flatpages.urls')),

]