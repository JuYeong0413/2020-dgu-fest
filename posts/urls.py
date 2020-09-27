from django.urls import path
from .views import *

app_name="posts"
urlpatterns = [
    path('gallery/', gallery, name="gallery"),
    path('new/', new, name="new"),
    path('create/', create, name="create"),
    path('update/<int:post_id>/', update, name="update"),
    path('delete/<int:post_id>/', delete, name="delete"),
    path('<int:post_id>/post_like/', post_like, name="post_like"),
]