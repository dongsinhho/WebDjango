from django.shortcuts import render
from django.template import loader
# from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'base/index.html')

def details(request):
    return render(request, 'base/details.html')

def profile(request):
    return render(request, 'base/profile.html')