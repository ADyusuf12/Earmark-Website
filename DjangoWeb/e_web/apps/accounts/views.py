from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from .forms import RegisterForm



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

def register(request):
    form = RegisterForm()
    
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/login')
        
    context = {'form': form}
    return render(request, 'register.html', context)
