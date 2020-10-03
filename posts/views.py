from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
import json, pdb
from django.core.paginator import Paginator
from django.db.models import Count
from django.core.exceptions import ValidationError

def gallery(request):
    posts=Post.objects.all().order_by('-created_at')
    sort = request.GET.get('sort','') 
    # paginator = Paginator(posts, 50)
    # page = request.GET.get('page')
    # posts = paginator.get_page(page)
    if sort == 'random':
        posts=Post.objects.all().order_by('?')
    # if sort == 'likes':
    #     posts = Post.objects.all().order_by('-like_user_set')
    return render(request, 'posts/gallery.html', {'posts':posts})

@login_required
def new(request):
    return render(request, 'posts/new.html')

@login_required
def create(request):
    if request.method == "POST" or "FILES":
        category = request.POST.get('category')
        title = request.POST.get('title')
        content = request.POST.get('content')
        mediafile = request.FILES.get('mediafile')
        mediatype = mediafile.content_type
        user = request.user
        post = Post.objects.create(category=category, title=title, content=content, mediafile=mediafile, mediatype=mediatype, user=user)
        
        try:
            post.full_clean()
            post.save()

        except ValidationError as e:
            # title= e.message_dict['title']
            # title = str(title)
            # title = title[2:len(title)-2]
            title = "공백 포함 최대 15자까지 입력 가능합니다."
            post.delete()
            return render(request, 'posts/new.html', {'title':title, 'post':post})

    return redirect('posts:gallery')

@login_required
def update(request, post_id):
    post = get_object_or_404(Post,pk=post_id)
    if post.user == request.user:
        if request.method == "POST":
            post.category = request.POST['category']
            post.title = request.POST['title']
            post.content = request.POST['content']
            if request.FILES.get('mediafile'):
                post.mediafile = request.FILES.get('mediafile')
                post.mediatype = request.FILES.get('mediafile').content_type
            
            try:
                post.full_clean()

            except ValidationError as e:
                # title= e.message_dict['title']
                # title = str(title)
                # title = title[2:len(title)-2]
                title = "최대 15자까지 입력 가능합니다."

                return render(request, 'posts/update.html', {'title':title, 'post':post})
            post.save()

            return redirect('posts:gallery')
        else:
            return render(request,'posts/update.html',{'post':post})
    else:
        return redirect('posts:gallery')

@login_required
def delete(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if post.user == request.user:
        post.delete()
    return redirect("posts:gallery")

def show(request, id):
    post = Post.objects.get(pk=id)
    return render(request, 'posts/show.html', {'post': post})
    
@login_required
def post_like(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post_like, post_like_created = post.like_set.get_or_create(user=request.user)

    if not post_like_created:
        post_like.delete()
        heart_icon = '<i class="far fa-heart"></i>'
    else:
        heart_icon = '<i class="fas fa-heart"></i>'

    context = {
        'heart_icon': heart_icon,
        'like_count': post.like_count,
    }

    return HttpResponse(json.dumps(context), content_type="application/json")
