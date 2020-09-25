from django.urls import path
from .views import *

app_name="users"
urlpatterns = [
    path('mypage/', mypage, name="mypage"),
    path('ps_change/', ps_change, name="ps_change"),
]