from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import CoffeeProduct, Post
from django.http import Http404

def home(request):
    # Get all coffee products from the database
    products = CoffeeProduct.objects.all()

    # Get all blog posts from the database
    posts_list = Post.published.all()

    # Paginate the blog posts
    paginator = Paginator(posts_list, 2)  # Show 2 posts per page
    page_number = request.GET.get('page')  # Get the current page number from the request

    try:
        posts = paginator.page(page_number)  # Get the posts for the current page
    except PageNotAnInteger:
        # If page is not an integer, deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g., 9999), deliver the last page
        posts = paginator.page(paginator.num_pages)

    # Pass the products and paginated posts to the template context
    return render(request, 'coffee/home.html', {
        'products': products,
        'posts': posts,  # Pass the paginated posts
    })

def blog(request):
    # Get all coffee products from the database

    # Pass the products to the template context
    return render(request, 'coffee/blog.html', {})

def post_detail(request, post):
    
    post = get_object_or_404(Post,
                                status=Post.Status.PUBLISHED,
                                slug=post)
    
    # Fetch recommended posts (e.g., 3 random posts excluding the current post)
    recommended_posts = Post.published.exclude(id=post.id).order_by('?')[:3]

    
    return render(request,
                'coffee/blog.html',
                            {'post': post,
                             'recommended_posts': recommended_posts,})