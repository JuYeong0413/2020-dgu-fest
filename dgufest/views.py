from django.shortcuts import render
from django import forms
from django.core.mail import EmailMessage

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def personal_data(request):
    return render(request, 'personal_data.html')

def service_terms(request):
    return render(request, 'service_terms.html')

def popup(request):
    return render(request, 'popup.html')

def Email(request):
    email = EmailMessage(
        'dgufest.com',                # 제목
    )
    email.send()