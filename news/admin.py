from django.contrib import admin

from .models import (
    Category,
    NewsPost
)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = ('name',)


@admin.register(NewsPost)
class NewsPostAdmin(admin.ModelAdmin):

    list_display = (
        'title',
        'category',
        'featured',
        'published',
        'created_at'
    )

    list_filter = (
        'category',
        'featured',
        'published'
    )

    prepopulated_fields = {}