from django.shortcuts import render, get_object_or_404

from .models import Post
# Create your views here.

def feed(request):
    post_list = Post.objects.order_by('-created_on')
    context = {'post_list': post_list}
    
    return render(request, 'feed.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post_detail': post}
    return render(request, 'post_detail.html', context)