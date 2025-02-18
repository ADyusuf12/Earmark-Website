from django.db import models
from django.contrib.auth.models import User


class Properties_Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)

    saved_by_users = models.ManyToManyField(User, related_name='saved_listings', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    views = models.PositiveIntegerField(default=0)
    title = models.CharField(max_length=150)
    price = models.IntegerField()
    parking_space = models.IntegerField(null=True, blank=True)
    bedrooms = models.IntegerField(null=True, blank=True)
    bathrooms = models.IntegerField(null=True, blank=True)
    size = models.IntegerField()
    address = models.CharField(max_length=200)
    certificate_num = models.CharField(max_length=255, default='')
    reference_num = models.CharField(max_length=255, default='')
    description = models.CharField(max_length=500)
    # video = models.FileField()
    google_map = models.CharField(max_length=500)


    STATUS_CHOICES = [
        ('For Rent', 'For Rent'),
        ('For Sale', 'For Sale'),
    ]
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    CATEGORY_CHOICES = [
        ('Flat/Apartment', 'Flat/Apartment'),
        ('House', 'House'),
        ('Plot/Land', 'Plot/Land'),
        ('Commercial', 'Commercial'),
    ]
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)

    LOCATION_CHOICES = [
        ('Kano', 'Kano'),
        ('Abuja', 'Abuja'),
    ]

    location = models.CharField(max_length=50, choices=LOCATION_CHOICES)

    def __str__(self):
        return self.title


class PropertyImage(models.Model):
    listing = models.ForeignKey(Properties_Listing, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/')

    def __str__(self):
        return f"Image for {self.listing.title}"