from django import forms
from .models import User
from allauth.account.forms import SignupForm
from .validation import *

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(max_length=10, label='이름')
    student_id = forms.CharField(validators=[validate_studentnumber], label='학번')
    agree_terms = forms.BooleanField(label='회원가입 시 해당 사이트의 서비스 이용약관 및 개인정보처리방침을 확인하였으며, 동의합니다.')
    
    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.agree_terms = self.cleaned_data['agree_terms']
        user.name = self.cleaned_data['name']        
        user.student_id = self.cleaned_data['student_id']
        user.save()
        return user