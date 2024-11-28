from django.http import HttpResponse, Http404

from django.shortcuts import render


data = [
    {'id': 0, 'name': 'image1.jpeg', 'type': 'jpeg'},
    {'id': 1, 'name': 'notes.txt', 'type': 'txt'},
    {'id': 2, 'name': 'image2.jpeg', 'type': 'jpeg'}
]


def home(request):
    return HttpResponse("Hello there")

def files(request):
    return render(request, 'files/files.html', {'files': data})

def file(request, file_id):
    f = next((item for item in data if item['id'] == file_id), None)
    if f is not None:
        return render(request, 'files/file.html', {'file': f})
    else:
        raise Http404("file does not exist")