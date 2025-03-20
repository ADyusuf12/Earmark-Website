from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile
from e_web.apps.public.models import Properties_Listing
from django.contrib import messages



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = get_object_or_404(UserProfile, pk=self.kwargs.get('pk', self.request.user.profile.pk))
        context['user_profile'] = user_profile
        
        user_listings = Properties_Listing.objects.filter(user=user_profile.user)
        context['user_listings'] = user_listings
        return context

@login_required
def ProfileSettings(request):
    user = request.user.profile
    form = ProfileForm(instance=user)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'accounts/profile-settings.html', context)

def register(request):
    """
    Handles user registration:
    - Displays the registration form.
    - Assigns the user to the selected group during registration.
    - Adds success messages upon successful registration.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Saves the user and assigns them to the selected group
            
            # Add a success message
            account_type = form.cleaned_data['account_type']
            messages.success(request, f"Account created successfully! You are registered as a {account_type}. Please log in.")
            
            # Redirect the user to the login page after successful registration
            return redirect('/accounts/login')
    else:
        form = RegisterForm()
    
    # Render the registration form page
    return render(request, 'register.html', {'form': form})

