# File_App/views.py
from django.shortcuts import render
from .models import File

def file_list(request):
    files = File.objects.all()
    return render(request, 'File_App/file_list.html', {'files': files})

