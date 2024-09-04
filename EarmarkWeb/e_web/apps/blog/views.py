from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment
from .forms import BlogPostForm


def blog(request):
    blog_posts = BlogPost.objects.all()
    for post in blog_posts:
        post.comment_count = Comment.objects.filter(blog_post=post).count()
    context = {
        'blog_posts': blog_posts,
    }
    return render(request, 'blog/blog.html', context)
    

def blog_details(request, post_id):
    # Retrieve the specific blog post based on post_id
    blog_post = get_object_or_404(BlogPost, id=post_id)

    # Retrieve related comments using the default related name (comment_set)
    comments = blog_post.comment_set.all()

    context = {'blog_post': blog_post, 'comments': comments}
    return render(request, 'blog/blog-details.html', context)

class BlogPostCreateView(CreateView, LoginRequiredMixin):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/create-blog.html'
    success_url = '/blog/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BlogPostUpdateView(UpdateView, LoginRequiredMixin):
    model = BlogPost
    form_class = BlogPostForm
    template_name = 'blog/update-blog.html'
    success_url = '/blog/'
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
class BlogPostDeleteView(DeleteView, LoginRequiredMixin):
    model = BlogPost
    template_name = 'blog/blogpost_confirm_delete.html'  # Create a confirmation template
    success_url = '/blog/' 