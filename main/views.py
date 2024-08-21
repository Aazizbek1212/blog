from django.shortcuts import render
from datetime import date, timedelta
from main.models import Post



def home_view(request):
    editors_pick = Post.objects.filter(editors_pick=True).last()
    trending_posts = Post.objects.filter(trending=True)[:3]
    week_ago = date.today() - timedelta(days=7)
    popular_post = Post.objects.filter(created_at__gte=week_ago).order_by('-hit_count')
    recent_posts = Post.objects.all()[:3]
    return render(request, 'index.html', {'editors_pick':editors_pick,
                                          'trending_posts':trending_posts,
                                          'popular_post':popular_post,
                                          'recent_posts':recent_posts})


def posts_view(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts':posts})


def post_detail_view(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'post_detail.html', {'post':post})