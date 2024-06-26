from django.shortcuts import render

from .models import Post
# Create your views here.

def post_home(request):
    post_list = Post.objects.order_by('-created_on')
    context = {'post_list': post_list}
    
    return render(request, 'user_create.html', context)