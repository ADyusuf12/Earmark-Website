from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm




class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
        
    context = {'form': form}
    return render(request, 'register.html', context)
