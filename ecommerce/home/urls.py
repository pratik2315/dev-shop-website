from django.contrib import admin
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name ='home'),
    path("about", views.aboutUs, name = 'about'),
    path("contact", views.contactUS, name = 'contact'),
    path("services", views.services, name = 'services'),

]