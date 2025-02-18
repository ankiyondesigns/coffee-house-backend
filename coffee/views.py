from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from .models import CoffeeProduct, Post
from django.http import Http404
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt

def home(request):
    # Get all coffee products from the database
    products = CoffeeProduct.objects.all()

    # Get all blog posts from the database
    posts_list = Post.published.all()

    # Paginate the blog posts
    paginator = Paginator(posts_list, 2)  # Show 2 posts per page
    page_number = request.GET.get('page')  # Get the current page number

    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)  # If page is not an integer, show first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # Show last page if out of range

    # Handle AJAX requests for pagination
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        posts_html = render_to_string('coffee/blog_posts_partial.html', {'posts': posts})
        pagination_html = render_to_string('coffee/pagination.html', {'posts': posts})
        return JsonResponse({
            'posts_html': posts_html,
            'pagination_html': pagination_html,
            'has_next': posts.has_next(),
            'has_previous': posts.has_previous(),
            'current_page': posts.number,
            'total_pages': paginator.num_pages,
        })

    # Render the full page for normal requests
    return render(request, 'coffee/home.html', {
        'products': products,
        'posts': posts,  # Pass paginated posts
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



@csrf_exempt
def upload_image(request):
    if request.method == "POST":
        image = request.FILES.get("image")
        path = default_storage.save(f"editorjs/images/{image.name}", ContentFile(image.read()))
        return JsonResponse({"success": 1, "file": {"url": f"/media/{path}"}})
    return JsonResponse({"success": 0, "error": "Upload failed"})

@csrf_exempt
def upload_video(request):
    if request.method == "POST":
        video = request.FILES.get("video")
        path = default_storage.save(f"editorjs/videos/{video.name}", ContentFile(video.read()))
        return JsonResponse({"success": 1, "file": {"url": f"/media/{path}"}})
    return JsonResponse({"success": 0, "error": "Upload failed"})