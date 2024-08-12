from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .models import UserProfile



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


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
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()    
            group = form.cleaned_data['group']        
            group.user_set.add(user)
            return redirect('/accounts/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
