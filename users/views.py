from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.hashers import check_password
from django.core.exceptions import PermissionDenied
from .views import *
from .forms import *
from django.contrib.auth.models import User


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

def signup(request):
    if request.user.is_authenticated:
        return redirect('posts:list')
        
    if request.method == 'POST':
        signup_form = UserCreationForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            Profile.objects.create(user=user) #프로필 생성
            auth_login(request, user)
            return redirect('posts:list')
    
    else:
        signup_form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'signup_form': signup_form})
