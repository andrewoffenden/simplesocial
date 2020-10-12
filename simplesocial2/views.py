from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'simplesocial2/home.html'