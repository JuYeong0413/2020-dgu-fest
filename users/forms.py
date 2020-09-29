from django import forms
from .models import User, Profile
from allauth.account.forms import SignupForm
from .validation import *

class MyCustomSignupForm(SignupForm):
    name = forms.CharField(max_length=10, label='이름')
    student_id = forms.CharField(validators=[validate_studentnumber], label='학번')

    def save(self, request):
        user = super(MyCustomSignupForm, self).save(request)
        user.name = self.cleaned_data['name']        
        user.student_id = self.cleaned_data['student_id']
        user.save()
        return user

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'student_id']