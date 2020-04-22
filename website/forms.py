from django import forms
from .models import JoinEvent
from django.views.generic import DetailView

class JoinEventForm(forms.ModelForm):
    class Meta:
        model = JoinEvent
        fields = ('event_id', 'f_name', 'l_name', 'email', 'mobile')
        labels = {
            'event_id': 'Event Name',
            'f_name': 'First Name',
            'l_name': 'Last Name',
            'email': 'Email Address',
            'mobile': 'Phone Number',
        }
        widgets = {
            'event_id': forms.TextInput(attrs={'readonly': 'readonly'}),
            'event_id': forms.HiddenInput()
        }


