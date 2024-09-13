from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm


def blog(request):
    blog_posts = BlogPost.objects.all()
    latest_posts = BlogPost.objects.order_by('date_created')
    for post in blog_posts:
        post.comment_count = Comment.objects.filter(blog_post=post).count()
    context = {
        'blog_posts': blog_posts,
        'latest_posts': latest_posts
    }
    return render(request, 'blog/blog.html', context)
    

def blog_details(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id)
    latest_posts = BlogPost.objects.order_by('date_created')
    comments = blog_post.comment_set.all()
    comment_form = CommentForm()
    
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.blog_post = blog_post
            new_comment.author = request.user
            new_comment.save()
            return redirect('blog/blog_details', post_id=post_id)
    context = {
        'blog_post': blog_post,
        'comments': comments,
        'comment_form': comment_form,
        'latest_posts': latest_posts
    }
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