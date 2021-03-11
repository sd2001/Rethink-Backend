
from django.contrib import admin
from django.urls import path, include
from Admins import views
from rest_framework.routers import DefaultRouter
from django.shortcuts import redirect


urlpatterns = [
    path('', include('Admins.urls')),
    path('admin/', admin.site.urls),
    path('manage/', include('Admins.urls')),
    path('doctors/', include('Practioners.urls')),
    path('patients/', include('Visitors.urls'))
]
