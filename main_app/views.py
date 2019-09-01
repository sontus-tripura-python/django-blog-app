from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post



def post_created(request):
    posts = Post.objects.filter(publish_date__lte=timezone.now()).order_by('-publish_date')
    stuff_for_frontend = {'posts':posts}
    return render (request, 'blog/post_created.html', stuff_for_frontend)
def post_details(request, pk):
    post = get_object_or_404(Post, pk=pk)
    stuff_for_frontend = { 'posts':post }
    return render (request, 'blog/post_details.html', stuff_for_frontend)
