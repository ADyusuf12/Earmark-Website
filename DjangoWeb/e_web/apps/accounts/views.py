from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render



class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'

def register(request):
    return render(request, 'register.html')
