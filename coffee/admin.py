from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CoffeeProduct, Post
from django.urls import path
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

class CoffeeProductAdmin(ModelAdmin):
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
class PostAdmin(ModelAdmin):
    list_display = ['title', 'slug', 'author', 'publish', 'status']
    list_filter = ['status', 'created', 'publish', 'author']
    search_fields = ['title', 'body']
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']

admin.site.register(CoffeeProduct, CoffeeProductAdmin)


class CustomAdminSite(admin.AdminSite):
    site_header = "Coffee Origins"
    site_title = "Website Admin"
    index_title = "Welcome Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('admin/', self.admin_view(self.index))
        ]
        return custom_urls + urls

    def each_context(self, request):
        context = super().each_context(request)
        context['extra_css'] = ['admin/css/custom_admin.css']
        return context

# Initialize custom admin site
admin_site = CustomAdminSite(name='custom_admin')

class CustomUserAdmin(UserAdmin):
    # Add the `compressed_fields` attribute
    compressed_fields = []


# Unregister the default UserAdmin
admin.site.unregister(User)

# Register your custom UserAdmin
admin.site.register(User, CustomUserAdmin)


admin.site.site_header = "Coffee Origins"
admin.site.site_title = "Website Admin"
admin.site.index_title = "Welcome Admin"