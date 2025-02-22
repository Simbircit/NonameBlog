from django.shortcuts import render, get_object_or_404
from .models import *
from django.core.paginator import Paginator
from datetime import date


def main(request):

    post_objects = Post.objects.order_by('-changed', '-published', 'title').filter(status='Public')
    paginator = Paginator(post_objects, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'noapp/main.html', {'posts': posts})


def main_old(request):

    post_objects = Post.objects.order_by('changed', 'published', 'title').filter(status='Public')
    paginator = Paginator(post_objects, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'noapp/main.html', {'posts': posts})


def main_day(request, day=date.today().day):

    post_objects = Post.objects.order_by('-changed', '-published', 'title').filter(status='Public', published__day=day)
    paginator = Paginator(post_objects, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'noapp/main.html', {'posts': posts})


def main_month(request, month=date.today().month):

    post_objects = Post.objects.order_by('-changed', '-published', 'title').filter(status='Public',
                                                                                   published__month=month)
    paginator = Paginator(post_objects, 3)
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'noapp/main.html', {'posts': posts})


def post_page(request, post_id):

    post = get_object_or_404(Post, id=post_id, status=Post.PostStatus.public)
    return render(request, 'noapp/post.html', {'post': post})
