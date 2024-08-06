from django.forms import ModelForm
from .models import Properties_Listing

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class Properties_ListingForm(ModelForm):
    class Meta:
        model = Properties_Listing
        fields = [
            "title",
            "price",
            "parking_space",
            "bedrooms",
            "bathrooms",
            "sqm",
            "address",
            "image",
            # "video",
            "google_map",
            "description",
            "status",
            "location",
        ]