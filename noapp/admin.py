from django.contrib import admin
from .models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'status', 'marker']
    list_filter = ['title', 'author', 'status', 'marker', 'id', 'changed', 'published', 'created']


@admin.register(Comment)
class PostAdmin(admin.ModelAdmin):
    list_display = ['name', 'published']
    list_filter = ['name', 'published', 'text']


admin.site.register(FeedBack)
