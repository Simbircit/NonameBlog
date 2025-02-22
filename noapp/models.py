from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):

    title = models.CharField(max_length=150)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    marker = models.SlugField()
    text = models.TextField(max_length=1000, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)
    created = models.DateTimeField(auto_created=True)
    published = models.DateTimeField(auto_now=True)
    changed = models.DateTimeField(auto_now_add=True)

    class PostStatus(models.TextChoices):

        draft = 'Draft'
        public = 'Public'

    status = models.CharField(max_length=6, choices=PostStatus.choices, default=PostStatus.draft)

    def __str__(self):

        return f"Post: {self.author} {self.title}"

    class Meta:

        ordering = ['title', 'author', 'status', 'marker']

    def get_absolute_url(self):

        return reverse('post_detail', kwargs={'pk': self.pk})


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, blank=True, default='Noname')
    text = models.CharField(max_length=300)
    published = models.DateTimeField(auto_now=True)


class FeedBack(models.Model):

    name = models.CharField(max_length=100, blank=True, default='Noname')
    text = models.CharField(max_length=300)
    mail = models.EmailField(max_length=50)
