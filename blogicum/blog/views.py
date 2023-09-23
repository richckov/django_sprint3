from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post, Category
import datetime
from blogicum.settings import COUNT_POST


def index(request) -> HttpResponse:
    """ Главная страница """
    post_list = Post.objects.select_related(
        'location',
        'category',
        'author',
    ).filter(
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.datetime.now(),
    ).order_by('-pub_date')[:COUNT_POST]
    context: dict = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk) -> HttpResponse:
    """ Страница постов """
    post = get_object_or_404(
        Post,
        pk=pk,
        is_published=True,
        category__is_published=True,
        pub_date__lte=datetime.datetime.now(),
    )
    context: dict = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug) -> HttpResponse:
    """ды Страница категорий """
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    post_list = Post.objects.filter(
        category=category,
        is_published=True,
        pub_date__lte=datetime.datetime.now(),
    )
    context: dict = {
        'category': category,
        'post_list': post_list,
    }
    return render(request, 'blog/category.html', context)
