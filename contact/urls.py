from django.contrib import admin
from django.urls import path
from . import views as contact_views
# from .views import ContactView

urlpatterns = [
    # path('contact/', ContactView.as_view(), name='contact')
    path('contact/', contact_views.contact, name='contact')
]
