from django.shortcuts import render, get_object_or_404
from .models import *


def main(request):

    posts = Post.objects.order_by('-changed', '-published', 'title')

    return render(request, 'noapp/main.html', {'posts': posts})


def post_page(request, post_id):

    post = get_object_or_404(Post, id=post_id, status=Post.PostStatus.public)
    return render(request, 'noapp/post.html', {'post': post})


# def blog(request, user_id):
#     pass
#
