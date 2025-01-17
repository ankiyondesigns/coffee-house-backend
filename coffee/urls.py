from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This points to our homepage
    path('blog/', views.blog, name='blog'),
    path('<slug:post>/', views.post_detail, name='post_detail')
]