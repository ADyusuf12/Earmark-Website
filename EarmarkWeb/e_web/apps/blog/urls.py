from django.urls import path
from .views import blog, blog_details, BlogPostCreateView, BlogPostDeleteView

app_name = "blog"

urlpatterns = [
    path("", blog, name = 'blog'),
    path('/<int:post_id>/', blog_details, name='blog_details'),
    path('create/', BlogPostCreateView.as_view(), name='create_blog'),
    path('<int:pk>/delete/', BlogPostDeleteView.as_view(), name='delete_blog'),
]