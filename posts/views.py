from django.shortcuts import render

# Create your views here.

def gallery(request):
    return render(request, 'posts/gallery.html')

def new(request):
    return render(request, 'posts/new.html')


