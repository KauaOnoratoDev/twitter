from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from .models import Post, User
from .forms import PostForm
# Create your views here.

def feed(request):
    post_list = Post.objects.order_by('-created_on')
    
    paginator = Paginator(post_list, 10)
    page = request.GET.get('page')
    
    post = paginator.get_page(page)
    context = {'post_list': post}
    
    return render(request, 'feed.html', context)

def post_detail(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'post_detail': post}
    return render(request, 'post_detail.html', context)

@login_required
def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = User.objects.get(pk=request.user.pk)  # Garante que `user` é uma instância de `User`
            post.save()
            return redirect('/')
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, 'new_post.html', context)

@login_required
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    context = {'delete_post': post}
    
    if request.method == 'POST':
        post.delete()
        return redirect('/')
    return render(request, 'delete_post.html', context)