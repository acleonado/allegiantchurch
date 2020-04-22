from django.shortcuts import render
from .models import Message
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings
from operator import sub
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def contact(request):
    form = ContactForm(request.POST or None)
    context = {
        'form': form,
    }  

    if request.method == 'POST':
        if form.is_valid():
            name = form.cleaned_data.get('name')
            from_email = form.cleaned_data.get('email')
            subject = form.cleaned_data.get('subject')
            msg = form.cleaned_data.get('msg')

            contact_message = "Name: %s \nMessage: %s \nEmail Address: %s" %(
                name,
                msg,
                from_email
            )
            send_mail(subject, contact_message, from_email, [settings.EMAIL_HOST_USER, from_email], fail_silently=False)
            messages.success(request, f"Thank you for connecting with us. We'll send our response to you on the email address you provided.")

            return HttpResponseRedirect(reverse('contact'))

    return render(request, 'contact.html', context)
    
