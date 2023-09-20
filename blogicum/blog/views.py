from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from blogicum.settings import COUNT_POST

from .models import Category, Post


def index(request) -> HttpResponse:
    """ Главная страница """
    post_list = Post.objects.select_related(
        'location',
        'category',
        'author',
    ).filter(
        category__is_published=True,
    ).order_by('-pub_date')[:COUNT_POST]
    context: dict = {'post_list': post_list}
    return render(request, 'blog/index.html', context)


def post_detail(request, pk) -> HttpResponse:
    """ Страница постов """
    post = get_object_or_404(
        Post,
        pk=pk,
        category__is_published=True,
    )
    context: dict = {'post': post}
    return render(request, 'blog/detail.html', context)


def category_posts(request, category_slug) -> HttpResponse:
    """ Страница категорий """
    category = get_object_or_404(
        Category,
        slug=category_slug,
    )
    # post_list = Post.objects.filter(
    #      category=category,
    #  )
    posts_in_category = Category.objects.get(id=1)
    posts = posts_in_category.posts_set.all()
    context: dict = {
        'category': category,
        'post_list': posts,
    }
    return render(request, 'blog/category.html', context)

