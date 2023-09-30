import datetime

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blogicum.settings import COUNT_POST

from .models import Category, Post  # PostManager


def index(request) -> HttpResponse:
    """ Главная страница """
    post_list = Post.active_objects.all()[:COUNT_POST]
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
    """ Страница категорий """
    category = get_object_or_404(
        Category.objects.filter(
            is_published=True,
            slug=category_slug,
        )
    )
    posts = category.posts.filter(
        is_published=True,
        pub_date__lte=datetime.datetime.now(),
    )
    context: dict = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)
