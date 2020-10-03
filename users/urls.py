from django.urls import path
from .views import *
from . import views

app_name="users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('likes/', like_list, name="like_list"),
    path('posts/', postlist, name="postlist"),
]