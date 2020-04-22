from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView, FormView, CreateView
from django.views.generic.edit import FormMixin, SingleObjectMixin
from .models import Schedule, Event, JoinEvent, Ministry, Service
from .forms import JoinEventForm
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseForbidden
from django.views import View
from django.contrib import messages
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin


class HomeView(ListView):
    template_name = 'home.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today()).order_by('date')[:4]
     
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['service_list'] = Service.objects.latest('id')
        return context 

class AboutView(ListView):
    model = Schedule
    template_name = 'about.html'

class MinistriesView(ListView):
    model = Ministry
    template_name = 'ministries.html'
    paginate_by = 6

class EventsView(ListView):
    model = Event
    template_name = 'events.html'
    paginate_by = 6

    def get_queryset(self):
        return Event.objects.filter(date__gte=date.today()).order_by('date')

class EventDetailView(DetailView):
    model = Event
    template_name = 'event_details.html'
    
    def get_context_data(self, **kwargs):

        # This is frequently used to pass all kinds of data to a template. 
        # The template can then render these components accordingly.
        context = super().get_context_data(**kwargs)
        context['form'] = JoinEventForm(initial={'event_id': self.object.id})
        return context

class JoinEventNow(SuccessMessageMixin, CreateView):
    form_class = JoinEventForm
    success_message = "Successfully registered to %(title)s Event"

    def get_success_message(self, cleaned_data):
        return self.success_message % dict(
            cleaned_data,
            title=self.object.event_id.title,
        )
    def get_success_url(self):
        return reverse('event-details', kwargs={'pk': self.object.event_id.pk})

class JoinEventView(View):
    def get(self, request, *args, **kwargs):
         view = EventDetailView.as_view()
         return view(request, *args, **kwargs) 

    def post(self, request, *args, **kwargs):
         view = JoinEventNow.as_view()
         return view(request, *args, **kwargs) 

class ServicesView(ListView):
    model = Service
    template_name = 'services.html'
    paginate_by = 6

    def get_queryset(self):
        return Service.objects.all().order_by('-date')



