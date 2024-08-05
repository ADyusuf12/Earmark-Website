from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail
from .forms import ContactForm
from e_web import settings
import bleach


# Create your views here.
def contact(request: HttpRequest) -> HttpResponse:
    
    if request.method == "GET":
        form = ContactForm()
    elif request.method =="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            subject = bleach.clean(form.cleaned_data["subject"])
            message = bleach.clean(form.cleaned_data["message"])
            send_mail(subject, message, email, [settings.EMAIL_HOST_USER])
            return render(request, "contact.html", {"form": form, "success": True})
        
    else:
        raise NotImplementedError
    
    return render(request, "contact.html", {"form": form})
    
    
        

