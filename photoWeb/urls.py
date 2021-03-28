from django.contrib import admin
from django.urls import path
from . import views


app_name = 'photoWeb'


urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('grid', views.grid, name='grid'),
    path('masonry', views.masonry, name='masonry'),
    path('blog', views.blog, name='blog'),
    path('single_post', views.single_post, name='single_post'),
    path('about', views.about, name='about'),
    path('get_message_from_user', views.get_message_from_user, name='get_message_from_user'),

    path('get_photo_page', views.get_photo_page, name='get_photo_page'),
    path('get_blog_page', views.get_blog_page, name='get_blog_page'),
]