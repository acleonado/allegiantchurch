from django import forms
from .models import Message
from django.views.generic import DetailView

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 50, required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'Full Name'}))
    email = forms.EmailField(required=True, label=False, widget=forms.EmailInput(attrs={'placeholder': 'Your Email Address'}))
    subject = forms.CharField(max_length = 100, required=True, label=False, widget=forms.TextInput(attrs={'placeholder': 'Subject'}))
    msg = forms.CharField(required=True, label=False, widget=forms.Textarea(attrs={'placeholder': 'Message'}))
    # class Meta:
    #     model = Message
    #     fields = ('name', 'email', 'subject', 'msg')
    #     labels = {
    #         'name': 'Name',
    #         'email': 'Email',
    #         'subject': 'Subject',
    #         'msg': 'Message',
    #     }
    #     widgets = {
    #         'event_id': forms.TextInput(attrs={'readonly': 'readonly'}),
    #         'event_id': forms.HiddenInput()
    #     }

