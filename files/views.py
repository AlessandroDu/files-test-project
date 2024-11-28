from django.http import HttpResponse, JsonResponse, Http404
from django.shortcuts import render, redirect

from .models import File
from .serializers import FileSerializer
from .forms import UploadForm

from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

def home(request):
    return HttpResponse("Hello there, you're at the home page.")

@api_view(['GET', 'POST'])
def files(request, format=None):
    if request.method == 'GET':
        data = File.objects.all()
        serializer = FileSerializer(data, many=True)
        return Response({'files': serializer.data})
    
    elif request.method == 'POST':
        serializer = FileSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PATCH', 'DELETE'])
def file(request, file_id, format=None):
    try:
        f = File.objects.get(pk=file_id)
    except File.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = FileSerializer(f)
        return Response({'file': serializer.data}, status=status.HTTP_200_OK)
    
    elif request.method == 'PATCH':
        serializer = FileSerializer(instance=f, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        f.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def edit(request, file_id):
    name = request.POST.get('name')
    file_type = request.POST.get('type')
    f = File.objects.get(pk=file_id)
    print(name, file_type, f)

    if f:
        if name:
            f.name = name
        if file_type:
            f.file_type = file_type
        f.save()
        return redirect(files)
    else:
        return redirect(files)

def delete(request, file_id):
    f = File.objects.get(pk=file_id)   
    if f:
        f.delete()
    return redirect(files)

def upload(request):
    form = UploadForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
    return redirect(files)
