from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def gallery(request):
    posts=Post.objects.all().order_by('?')
    return render(request, 'posts/gallery.html', {'posts':posts})

def new(request):
    return render(request, 'posts/new.html')

def create(request):
    if request.method == "POST":
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        mediafile = request.FILES.get('mediafile')
        mediatype = mediafile.content_type
        Post.objects.create(category=category, title=title, content=content, mediafile=mediafile, mediatype=mediatype)
    return redirect('posts:gallery')

