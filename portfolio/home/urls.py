from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('project', project, name="project"),
    path('contact', contact, name="contact"),
]
