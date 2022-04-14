from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here. Everytime you want a new view for your website you will need to add a view function here.


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse("New Products")
