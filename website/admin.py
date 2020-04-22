from django.contrib import admin
from .models import Schedule, Event, JoinEvent, Ministry, Service
from django.db import models

admin.site.register(Schedule)
admin.site.register(Event)
admin.site.register(JoinEvent)
admin.site.register(Ministry)
admin.site.register(Service)


