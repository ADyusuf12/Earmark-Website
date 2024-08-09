from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth.models import Group, User



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

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
