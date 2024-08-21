from django.urls import path

from main.views import home_view, post_detail_view, posts_view


urlpatterns = [
    path('', home_view, name='home'),
    path('posts/', posts_view, name='posts'),
    path('post_detail/<int:pk>/', post_detail_view, name='post_detail'),
]
