from django.forms import ModelForm
from .models import Properties_Listing

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