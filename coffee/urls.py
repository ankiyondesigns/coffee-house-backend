from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This points to our homepage
    path('blog/', views.blog, name='blog'),
    path('<slug:post>/', views.post_detail, name='post_detail'),

    path("upload-image/", views.upload_image, name="upload_image"),
    path("upload-video/", views.upload_video, name="upload_video"),
]