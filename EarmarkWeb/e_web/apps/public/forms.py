from django.forms import ModelForm
from .models import Properties_Listing
from django import forms

class Properties_ListingForm(ModelForm):
    class Meta:
        model = Properties_Listing
        fields = [
            "title",
            "category",
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
        

class PropertySearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False)
    status = forms.CharField(max_length=50, required=False)
    category = forms.CharField(max_length=50, required=False)
    bedrooms = forms.IntegerField(required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    min_sqm = forms.IntegerField(required=False)
    max_sqm = forms.IntegerField(required=False)
