from django.shortcuts import render, redirect, get_object_or_404
from .models import *

# Create your views here.

def gallery(request):
    posts=Post.objects.all().order_by('-created_at')
    sort = request.GET.get('sort','') 
    if sort == 'random':
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
        user = request.user
        Post.objects.create(category=category, title=title, content=content, mediafile=mediafile, mediatype=mediatype, user=user)
    return redirect('posts:gallery')

def update(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    if request.method == "POST":
        post.category = request.POST['category']
        post.title = request.POST['title']
        post.content = request.POST['content']
        if request.FILES.get('mediafile'):
            post.mediafile = request.FILES.get('mediafile')
            post.mediatype = request.FILES.get('mediafile').content_type
        post.save()
        return redirect('posts:gallery')
    return render(request,'posts/update.html',{'post':post})

def delete(request, post_id): 
	post = get_object_or_404(Post, pk=post_id) 
	post.delete()
	return redirect("posts:gallery")




