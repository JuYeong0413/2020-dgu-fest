from django import forms
from .models import User, Profile
from allauth.account.forms import SignupForm
from .validation import *
from django.contrib.auth.models import User

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(max_length=10, label='이름')
    student_id = forms.CharField(label='학번')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.name = self.cleaned_data['name']        
        user.profile.student_id = self.cleaned_data['student_id']
        user.save()
        return user
