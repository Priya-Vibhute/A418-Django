from django.shortcuts import render
from .models  import Product
# Create your views here.

def products(request):
    return render(request,"products.html")

def royalCanin(request):
    products=Product.customManager.royalCanin()
    return render(request,"products.html",{"products":products})