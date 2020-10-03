from django import forms
from .models import User, Profile
from allauth.account.forms import SignupForm
from .validation import *
from django.contrib.auth.models import User

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(max_length=10, label='이름', widget=forms.TextInput(attrs={'placeholder': '이름'}))
    student_id = forms.IntegerField(label='학번', widget=forms.TextInput(attrs={'placeholder': '10자리 학번'}))
    phone_number = forms.IntegerField(label='핸드폰번호', widget=forms.TextInput(attrs={'placeholder': '숫자만 입력해주세요.'}))

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if Profile.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError('이미 존재하는 전화번호 입니다.')
        return phone_number

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.profile.name = self.cleaned_data['name']
        user.profile.student_id = self.cleaned_data['student_id']
        user.profile.phone_number = self.cleaned_data['phone_number']
        user.save()
        return user

