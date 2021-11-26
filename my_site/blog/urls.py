from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("posts", views.posts, name="posts"),
    path("<int:selected_post>", views.post_by_number),
    path("<str:selected_post>", views.post, name="my_post")
]
