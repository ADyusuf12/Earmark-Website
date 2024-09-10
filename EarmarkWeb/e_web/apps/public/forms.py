from django.forms import ModelForm
from .models import Properties_Listing, PropertyImage
from django import forms

class Properties_ListingForm(ModelForm):
    class Meta:
        model = Properties_Listing
        fields = [
            "title",
            "description",
            "address",
            "certificate_num",
            "reference_num", 
            "google_map",
            "location",
            "status",
            "category",
            "size",
            "price",
            "bedrooms",
            "bathrooms",
            "parking_space",
            # "video",,
        ]
        help_texts = {
            'size': 'Size in squaremeter'
        }
        
class PropertyImageForm(forms.ModelForm):
    class Meta:
        model = PropertyImage
        fields = ['image']
        

class PropertySearchForm(forms.Form):
    location = forms.CharField(max_length=100, required=False)
    status = forms.CharField(max_length=50, required=False)
    category = forms.CharField(max_length=50, required=False)
    bedrooms = forms.IntegerField(required=False)
    min_price = forms.IntegerField(required=False)
    max_price = forms.IntegerField(required=False)
    min_sqm = forms.IntegerField(required=False)
    max_sqm = forms.IntegerField(required=False)
