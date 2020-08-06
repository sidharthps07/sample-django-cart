from django.http import HttpResponse
from django.shortcuts import render
from .models import products


# Create your views here.
def index(request):
    product=products.objects.all()
    return render(request,'index.html',{'products':product})
    #return HttpResponse("<h1>Welcome to Django</h1>")
def about(request):
    return HttpResponse("<h1>about page</h1>")
def contacts(request):
    return HttpResponse("<h1>contact page</h1>")
