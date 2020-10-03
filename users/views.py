from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from posts.models import Like, Post

def mypage(request):
    return render(request, 'users/mypage.html')


@login_required
def like_list(request):
    likes = Like.objects.filter(user=request.user)
    return render(request, 'users/like_list.html', {'likes': likes})


@login_required
def postlist(request):
    user = request.user
    context = {'posts' : Post.objects.filter(user=user)}
    return render(request, 'users/postlist.html', context)