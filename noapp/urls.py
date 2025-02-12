from django.contrib.auth.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='NoNameBlog'),
    path('post/<int:post_id>', views.post_page, name='post')
]
