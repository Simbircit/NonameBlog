from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import *
from .forms import *
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
    comments = Comment.objects.filter(post__id=post_id).order_by('-published')
    if request.method == 'POST':
        form = CommentForm(request.POST)
        comment = Comment()
        comment.post = get_object_or_404(Post, id=post_id)
        comment.text = request.POST.get('text')
        comment.name = request.POST.get('name')
        comment.save()
    else:
        form = CommentForm()

    return render(request, 'noapp/post.html', {'post': post, 'comments': comments, 'form': form})


def feed_back(request):

    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = FeedBackForm()

    return render(request, 'noapp/feedback.html', {'form': form})
