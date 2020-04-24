from django.db import models
from django.forms.fields import TimeField
from datetime import date
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from PIL import Image
from phone_field import PhoneField
from django.urls import reverse, reverse_lazy



@property
def is_past_due(self):
    return date.today() > self.date

class Schedule(models.Model):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    desc = RichTextField(max_length=100, blank=True)
    address = models.CharField(max_length=500, blank=True)
    time_from = models.TimeField()

    def __str__(self):
        return self.title + ' | ' + str(self.location)

class Event(models.Model):
    title = models.CharField(max_length=40)
    location = models.CharField(max_length=40)
    desc = RichTextField(max_length=1000)
    address = models.CharField(max_length=500)
    date = models.DateField()
    time = models.TimeField()
    img = models.ImageField(default='website/default.jpg', upload_to='website/events')

    def clean(self):
        if self.date != None:
            if is_past_due:
                raise ValidationError('Date must not be past')

    def __str__(self):
        return self.title + ' | ' + self.location

class JoinEvent(models.Model):
    event_id = models.ForeignKey(Event, on_delete = models.CASCADE)
    f_name = models.CharField(max_length = 50)
    l_name = models.CharField(max_length = 50)
    email = models.EmailField()
    mobile = PhoneField(max_length = 10, E164_only=False)

    def __str__(self):
        return self.f_name + ' ' + self.l_name + ' | ' + str(self.event_id)

class Ministry(models.Model):
    title = models.CharField(max_length = 50)
    leader = models.CharField(max_length = 50)
    img =  models.ImageField(default='website/default.jpg', upload_to='website/ministry')

    def __str__(self):
        return self.title + ' | ' + str(self.leader)

class Service(models.Model):
    date = models.DateField()
    title = models.CharField(max_length = 100)
    pastor = models.CharField(max_length = 50)
    video_link = models.URLField(max_length = 400)
    video_thumbnail = models.ImageField(default='website/default.jpg', upload_to='website/sermon')

    def __str__(self):
        return str(self.date) + ' | ' + str(self.title)