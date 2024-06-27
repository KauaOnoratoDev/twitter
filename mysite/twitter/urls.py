from django.urls import path
from . import views

urlpatterns = [
    path('', views.feed, name='feed'),
    path('post/<int:id>', views.post_detail, name='post_detail'),
]