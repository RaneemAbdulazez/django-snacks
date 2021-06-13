from django.views.generic import TemplateView
from django.shortcuts import render


class HomePageView(TemplateView):
    template_name="home.html" #load this template


class AboutPageView(TemplateView):
    template_name="about.html" #load this template
    