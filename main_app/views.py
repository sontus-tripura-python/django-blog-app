from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from .forms import PostForm
from .models import Post



def post_created(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    stuff_for_frontend = {'posts': posts}
    return render (request, 'blog/post_created.html', stuff_for_frontend)
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = { 'posts': post }
    return render (request, 'blog/post_details.html', stuff_for_frontend)
def post_edit(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.publish_date = timezone.now()
            post.save()
            return redirect('post_details', pk=post.pk)
    else:
        form = PostForm()
        stuff_for_frontend = {'form': form}
    return render (request, 'blog/post_edit.html', stuff_for_frontend)
