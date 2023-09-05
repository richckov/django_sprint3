from django.contrib import admin

from .models import Category, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'slug',
        'is_published',
        'created_at',
    )
    list_editable = (
        # 'is_published',
        # 'category',
    )
    search_fields = (
        'title',
        'category',
    )
    # list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )
    search_fields = ('name',)
    list_display_links = ('name',)
    empty_value_display = 'Не задано'


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'text',
        'pub_date',
        'author',
        'location',
        'category',
    )
    list_editable = (
        # 'is_published',
        'category',
    )
    search_fields = ('title',)
    list_filter = ('category',)
    list_display_links = ('title',)
    empty_value_display = 'Не задано'


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
