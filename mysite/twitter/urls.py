from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
    path('newpost/', views.new_post, name='new_post'),
    path('post/deletepost/<int:id>', views.delete_post, name='delete_post'),
]