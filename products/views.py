from django.http import HttpResponse
from django.shortcuts import render

# Create your views here. Everytime you want a new view for your website you will need to add a view function here.


def index(request):
    return HttpResponse("Hello World!")


def new(request):
    return HttpResponse("New Products")
