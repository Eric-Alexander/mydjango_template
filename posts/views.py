from django.shortcuts import render
from django.http import HttpResponse

def posts_readall(request):
    return render(request, "index.html", {})

def posts_create(request):
    return HttpResponse("<h1>Create</h1>")

def posts_read(request):
    return HttpResponse("<h1>Read</h1>")

def posts_update(request):
    return HttpResponse("<h1>Update</h1>")

def posts_delete(request):
    return HttpResponse("<h1>delete</h1>")
