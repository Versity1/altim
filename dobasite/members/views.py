from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

#home view
def home(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

#login view
def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())

# register view
def register(request):
    template = loader.get_template('register.html')
    return HttpResponse(template.render())

# profile view
def profile(request):
    template = loader.get_template('profile.html')
    return HttpResponse(template.render())

# table view
def table(request):
    template = loader.get_template('table.html')
    return HttpResponse(template.render())
