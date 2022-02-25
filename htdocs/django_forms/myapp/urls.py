from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('quick', views.quick),
    path('custom', views.custom),
    path('contact', views.contact),
]
