from django.contrib.auth.models import User
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .validation import *
from django import forms

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(verbose_name='name', max_length=10)
    student_id = models.PositiveIntegerField(validators=[validate_studentnumber], null=True)
    birth_date = models.DateTimeField(verbose_name='birth_date', null=True, blank=True)
    
    GENDER_CHOICES ={
        ('F', 'Female'),
        ('M', 'Male'),
    }
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True)
    phone_number = models.PositiveIntegerField(verbose_name='phone number', unique=True, null=True, validators=[validate_phonenumber])

    
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    
@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
