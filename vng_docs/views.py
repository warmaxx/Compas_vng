from django.shortcuts import render
from vng_docs.models import Folder, File


def index(request):
    files = File.objects.all()
    folders = Folder.objects.all()
    context = {
        'files': files,
        'folders': folders,
    }
    return render(request, 'vng_docs/index.html', context)


def folder(request, folder_id):
    files = File.objects.all().filter(folder_id=folder_id)
    folders = Folder.objects.all()
    context = {
        'files': files,
        'folders': folders,
    }
    return render(request, 'vng_docs/index.html', context)
