from django.shortcuts import render, get_object_or_404
from .models import CoffeeProduct, Post
from django.http import Http404

def home(request):
    # Get all coffee products from the database
    products = CoffeeProduct.objects.all()

    # Get all blog posts from the database
    posts = Post.published.all()

    # Pass the products to the template context
    return render(request, 'coffee/home.html', {'products': products, 'posts': posts})

def blog(request):
    # Get all coffee products from the database

    # Pass the products to the template context
    return render(request, 'coffee/blog.html', {})

def post_detail(request, post):
    
    post = get_object_or_404(Post,
                                status=Post.Status.PUBLISHED,
                                slug=post)

    
    return render(request,
                'coffee/blog.html',
                            {'post': post})