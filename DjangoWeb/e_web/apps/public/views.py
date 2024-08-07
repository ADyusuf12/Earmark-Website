from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Properties_Listing
from .forms import Properties_ListingForm





def index(request):
    listings = Properties_Listing.objects.order_by('id')
    context = {
        "listings": listings
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')


def error_page(request):
    return render(request, '404.html')

def properties_list(request):
    listings = Properties_Listing.objects.all()
    context = {
        "listings": listings
    }
    return render(request, 'properties.html', context)

def properties_list_retrieve(request, pk):
    listing = Properties_Listing.objects.get(id=pk)
    context = {
        "listing": listing
    }
    return render(request, 'properties-detail.html', context)

@login_required(redirect_field_name="accounts/login")
def properties_list_create(request):
    form = Properties_ListingForm()
    if request.method == "POST":
        form = Properties_ListingForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/properties_list")
    
    context = {
        "form": form
    }
    return render(request, 'create.html', context)

@login_required(redirect_field_name="accounts/login")
def properties_list_update(request, pk):
    listing = Properties_Listing.objects.get(id=pk)
    form = Properties_ListingForm(instance=listing)
    
    if request.method == "POST":
        form = Properties_ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/properties_list")
    
    context = {
        "form": form
    }
    return render(request, 'update.html', context)

@login_required(redirect_field_name="accounts/login")
def deleteListing(request, pk):
    listing = Properties_Listing.objects.get(id=pk)
    listing.delete()
    return redirect("/properties_list")
