from django.core.mail import EmailMessage
from .forms import ContactForm
from django.conf import settings
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
import bleach

def contact(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = bleach.clean(form.cleaned_data["name"])
            email = bleach.clean(form.cleaned_data["email"])
            subject = bleach.clean(form.cleaned_data["subject"])
            message = bleach.clean(form.cleaned_data["message"])
            
            # Append the sender's email to the message
            message += f"\n\n--\nSent from: {email}"
            
            # Create and send email
            email_message = EmailMessage(
                subject,  # Subject of the email
                message,  # Message body
                settings.EMAIL_HOST_USER,  # From email
                [settings.EMAIL_HOST_USER],  # To email
                reply_to=[email]  # Reply-to email
            )
            email_message.send(fail_silently=False)
            
            return render(request, "contact.html", {"form": form, "success": True})
    else:
        raise NotImplementedError
    
    return render(request, "contact.html", {"form": form})
