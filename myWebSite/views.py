from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
def index(request):
    # redirect_path = reverse("home-page")
    return HttpResponseRedirect("/home/")
