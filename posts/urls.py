from django.urls import path
from .views import *

app_name="posts"
urlpatterns = [
    path('gallery/', gallery, name="gallery"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
]