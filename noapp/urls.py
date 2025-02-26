from django.contrib.auth.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='NoNameBlog'),
    path('old/', views.main_old, name='old'),
    path('month/', views.main_month, name='month'),
    path('day/', views.main_day, name='day'),
    path('feedback/', views.feed_back, name='feedback'),
    path('post/<int:post_id>', views.post_page, name='post')
]
