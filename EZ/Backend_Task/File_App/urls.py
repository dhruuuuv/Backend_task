# File_App/urls.py
from django.urls import path
from .views import file_list

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', file_list, name='file_list'),
    path('admin/', admin.site.urls),
    path('file-app/', include('File_App.urls')),
    # Add more app URLs as needed
]

