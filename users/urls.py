from django.urls import path
from .views import *
from . import views


app_name="users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('password_change/', password_change, name="password_change"),
]