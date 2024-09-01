from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.http import HttpResponseForbidden, JsonResponse
from django.contrib.auth.decorators import login_required
from . decorators import user_has_permission
from .models import Properties_Listing
from .forms import Properties_ListingForm, PropertySearchForm
from django.views.generic import ListView






def index(request):
    latest_listings = Properties_Listing.objects.order_by('-created_at')[:3]
    context = {
        "latest_listings": latest_listings
        
    }
    return render(request, 'index.html', context)

def blog(request):
    return render(request, 'blog.html')

def gallery(request):
    return render(request, 'gallery.html')


def error_page(request):
    return render(request, '404.html')

def properties_list(request):
    form = PropertySearchForm(request.GET or None)
    listings = Properties_Listing.objects.all()

    if form.is_valid():
        if form.cleaned_data['location']:
            listings = listings.filter(location__icontains=form.cleaned_data['location'])
        if form.cleaned_data['status']:
            listings = listings.filter(status__icontains=form.cleaned_data['status'])
        if form.cleaned_data['category']:
            listings = listings.filter(category__icontains=form.cleaned_data['category'])
        if form.cleaned_data['bedrooms'] is not None:
            listings = listings.filter(bedrooms=form.cleaned_data['bedrooms'])
        if form.cleaned_data['min_price'] is not None:
            listings = listings.filter(price__gte=form.cleaned_data['min_price'])
        if form.cleaned_data['max_price'] is not None:
            listings = listings.filter(price__lte=form.cleaned_data['max_price'])
        if form.cleaned_data['min_sqm'] is not None:
            listings = listings.filter(sqm__gte=form.cleaned_data['min_sqm'])
        if form.cleaned_data['max_sqm'] is not None:
            listings = listings.filter(sqm__lte=form.cleaned_data['max_sqm'])
            
    
    # if 'status' in request.GET:
    #     listings = listings.filter(status__iexact=request.GET['status'])
        

    paginator = Paginator(listings, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    # Fetch popular properties
    popular_listings = Properties_Listing.objects.order_by('-views')[:3]
    
    
    context = {
        "listings": page_obj,
        "form": form,
        "page_obj": page_obj,
        "popular_listings": popular_listings
    }
    return render(request, 'properties.html', context)

def properties_list_retrieve(request, pk):
    listing = Properties_Listing.objects.get(id=pk)
    listing.views += 1
    listing.save()
    popular_listings = Properties_Listing.objects.order_by('-views')[:3]

    # Retrieve the users who have saved this property
    saved_users = listing.saved_by_users.all()

    context = {
        "listing": listing,
        "popular_listings": popular_listings,
        "saved_users": saved_users,
    }
    return render(request, 'properties-detail.html', context)





class SavedListingsView(ListView):
    model = Properties_Listing
    template_name = 'saved_listings.html'
    context_object_name = 'saved_listings'

    def get_queryset(self):
        # Filter saved properties for the current user
        return Properties_Listing.objects.filter(saved_by_users=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve popular properties (e.g., top 3 by views)
        popular_listings = Properties_Listing.objects.order_by('-views')[:3]
        context['popular_listings'] = popular_listings
        return context


def save_listing_view(request, pk):
    if request.method == 'POST' and request.user.is_authenticated:
        listing = get_object_or_404(Properties_Listing, id=pk)
        listing.saved_by_users.add(request.user)
        return JsonResponse({'message': 'Property saved successfully'})
    else:
        return JsonResponse({'error': 'Unauthorized'}, status=401)


@login_required(redirect_field_name="accounts/login")
@user_has_permission('add_properties_listing')
def properties_list_create(request):
    if request.method == "POST":
        form = Properties_ListingForm(request.POST, files=request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect("/properties_list")
    else:
        form = Properties_ListingForm()
    
    context = {
        "form": form
    }
    return render(request, 'create.html', context)

@login_required(redirect_field_name="accounts/login")
@user_has_permission('change_properties_listing')
def properties_list_update(request, pk):
    listing = get_object_or_404(Properties_Listing, id=pk)
    
    if listing.user != request.user:
        return HttpResponseForbidden("You are not allowed to edit this listing.")
    
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
@user_has_permission('delete_properties_listing')
def deleteListing(request, pk):
    listing = get_object_or_404(Properties_Listing, id=pk)
    
    if listing.user != request.user:
        return HttpResponseForbidden("You are not allowed to delete this listing.")
    
    listing.delete()
    return redirect("/properties_list")
