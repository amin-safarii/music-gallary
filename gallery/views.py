from django.shortcuts import render, get_object_or_404
from django.db import models
from django.core.paginator import Paginator
from .models import Post, Category, Artist

POSTS_PER_PAGE = 6

def get_common_context():
    return {
        'categories': Category.objects.all().order_by('id'),
        'artist': Artist.objects.first(),
    }

def home(request):
    context = get_common_context()
    context['featured_posts'] = Post.objects.filter(main_post=True).order_by('-created_at')[:4]
    context['about_artist'] = context['artist']
    return render(request, 'gallery/home.html', context)

def post_list(request):
    context = get_common_context()
    all_posts = Post.objects.all().order_by('-created_at')
    paginator = Paginator(all_posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context['posts'] = page_obj
    context['page_obj'] = page_obj
    context['paginator'] = paginator
    return render(request, 'gallery/post_list.html', context)

def category_list(request, slug):
    context = get_common_context()
    category = get_object_or_404(Category, slug=slug)
    all_posts = Post.objects.filter(category=category).order_by('-created_at')
    paginator = Paginator(all_posts, POSTS_PER_PAGE)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)
    context['current_category'] = category
    context['posts'] = page_obj
    context['page_obj'] = page_obj
    context['paginator'] = paginator
    return render(request, 'gallery/post_list.html', context)

def post_detail(request, slug):
    context = get_common_context()
    post = get_object_or_404(Post, slug=slug)
    context['post'] = post
    return render(request, 'gallery/post_detail.html', context)


def search(request):
    context = get_common_context()
    query = request.GET.get('q', '').strip()
    results = []
    if query:
        results = Post.objects.filter(
            models.Q(title__icontains=query) |
            models.Q(content__icontains=query) |
            models.Q(category__title__icontains=query)
        ).distinct().order_by('-created_at')
    context['query'] = query
    context['results'] = results
    context['result_count'] = len(results)
    return render(request, 'gallery/search_results.html', context)


def about(request):
    context = get_common_context()
    context['all_posts_count'] = Post.objects.count()
    return render(request, 'gallery/about.html', context)
