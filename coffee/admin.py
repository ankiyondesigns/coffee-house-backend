from django.utils.html import format_html
from django.contrib import admin
from .models import CoffeeProduct, Post

class CoffeeProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'measurement_grams', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('price', 'measurement_grams')
    ordering = ('price',)
    list_per_page = 10

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius:5px;" />', obj.image.url)
        return 'No image'

    image_preview.short_description = 'Image'


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(CoffeeProduct, CoffeeProductAdmin)
