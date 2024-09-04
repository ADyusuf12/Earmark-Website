from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    
    title = models.CharField(max_length=64)
    description = models.CharField(max_length=90)
    body = models.CharField(max_length=300)
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.ImageField() 
    
    def formatted_date(self):
        
        return self.date_created.strftime("%d %B, %y")
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    
    
    def formatted_timestamp(self):
        
        formatted_date = self.timestamp.strftime("%d %B, %y")
        # Format the time as 12-hour clock (e.g., "03:30 PM")
        formatted_time = self.timestamp.strftime("%I:%M %p")
        return f"{formatted_date} at {formatted_time}"

    def __str__(self):
        return f"Comment by {self.author} on {self.blog_post.title}"