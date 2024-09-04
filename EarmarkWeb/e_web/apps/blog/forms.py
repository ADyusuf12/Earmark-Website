from django import forms
from .models import BlogPost, Comment

class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['title', 'body', 'image', 'description']
        

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Only the comment content field

    def __init__(self, *args, **kwargs):
        self.blog_post = kwargs.pop('blog_post')  # Get the blog post instance
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        comment = super().save(commit=False)
        comment.blog_post = self.blog_post  # Associate the comment with the blog post
        if commit:
            comment.save()
        return comment