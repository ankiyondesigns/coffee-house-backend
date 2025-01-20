from django.utils.html import format_html
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import CoffeeProduct, Post
from django.urls import path
from unfold.admin import ModelAdmin
from django.contrib.auth.models import User

from unfold.forms import AdminPasswordChangeForm, UserChangeForm, UserCreationForm

class CoffeeProductAdmin(ModelAdmin):
    list_display = ('name', 'price', 'measurement_unit','measurement_value', 'image_preview')
    search_fields = ('name', 'description')
    list_filter = ('price', 'measurement_unit', 'measurement_value')
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
    readonly_fields = ['author']  # Make the author field read-only

    def save_model(self, request, obj, form, change):
        """
        Automatically set the logged-in user as the author for new posts.
        """
        if not obj.pk:  # If this is a new post
            obj.author = request.user
        super().save_model(request, obj, form, change)

    def author(self, obj):
        """
        Display the name of the logged-in user in the read-only author field.
        """
        if obj.author:
            return obj.author.username  # Display the username of the user
        return "No author"

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
        context['favicon'] = format_html('<link rel="icon" href="{}/static/favicon/favicon.ico" type="image/x-icon">', request.build_absolute_uri('/'))
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


admin.site.site_header = "Hello Coffee"
admin.site.site_title = "Website Admin"
admin.site.index_title = "Welcome Admin"