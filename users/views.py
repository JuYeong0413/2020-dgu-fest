from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from posts.models import Like
from posts.models import Post

def mypage(request):
    return render(request, 'users/mypage.html')

def password_change(request):
    context= {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password,user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request,user)
                return redirect("users:myblog")
            else:
                context.update({'error':"새로운 비밀번호를 다시 확인해주세요."})
    else:
        context.update({'error':"현재 비밀번호가 일치하지 않습니다."})
    return render(request, 'users/password_change.html')

@login_required
def like_list(request):
    likes = Like.objects.filter(user=request.user)
    return render(request, 'users/like_list.html', {'likes': likes})


def postlist(request):
    user = request.user
    context = {'posts' : Post.objects.filter(user=user)}
    return render(request, 'users/postlist.html', context)