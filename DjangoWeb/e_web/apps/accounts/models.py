from django.db import models
from django.contrib.auth.models import User

class UserInterest(models.Model):
    name = models.CharField(max_length=64, unique=True)
    
    def __str__(self):
        return self.name





class UserProfile(models.Model):
    # owner
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    
    # settings
    full_name_displayed = models.BooleanField(default=True)


    # details

    first_name = models.CharField(max_length=64, blank=True)
    last_name = models.CharField(max_length=64, blank=True)
    email = models.EmailField()
    username = models.CharField(max_length=64, null=True, blank=True)
    
    profile_pic = models.ImageField(default="default-pic.jpg", null=True, blank=True)
    
    
    bio = models.CharField(max_length=500, blank=True, null=True)
    phone = models.CharField(max_length=64, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    
    interests = models.ManyToManyField(UserInterest, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    
    def __str__(self):
        return self.user.username
    
    
    
    

    
    
    