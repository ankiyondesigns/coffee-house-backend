from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This points to our homepage
    path('blog/', views.blog, name='blog'),
    path('<int:id>/', views.post_detail, name='post_detail')
]