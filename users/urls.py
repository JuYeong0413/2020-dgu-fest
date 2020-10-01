from django.urls import path
from .views import *
from . import views

app_name="users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('password_change/', password_change, name="password_change"),
    path('like_list/', like_list, name="like_list"),
    path('postlist/', postlist, name="postlist"),
]