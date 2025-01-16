from django.utils.html import format_html
from django.contrib import admin
from .models import CoffeeProduct

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

admin.site.register(CoffeeProduct, CoffeeProductAdmin)
