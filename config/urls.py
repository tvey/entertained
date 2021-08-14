from django.contrib import admin
from django.urls import path

from entertainments.views import index, filter_data, everything

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='home'),
    path('f/', filter_data, name='filter'),
    path('everything/', everything, name='everything'),
]
