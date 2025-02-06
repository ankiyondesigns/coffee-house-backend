from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
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

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # If it's an AJAX request, return JSON data
        posts_html = render_to_string('coffee/blog_posts_partial.html', {'posts': posts})
        return JsonResponse({
            'posts_html': posts_html,
            'has_next': posts.has_next(),
            'has_previous': posts.has_previous(),
            'current_page': posts.number,
            'total_pages': paginator.num_pages,
        })

    # If it's a regular request, render the full page
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