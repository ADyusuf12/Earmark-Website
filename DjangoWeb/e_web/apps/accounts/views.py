from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from .forms import RegisterForm, ProfileForm
from django.contrib.auth.decorators import login_required
from .models import UserProfile



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_profile = get_object_or_404(UserProfile, pk=self.kwargs.get('pk', self.request.user.profile.pk))
        context['user_profile'] = user_profile
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
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('/accounts/login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})
