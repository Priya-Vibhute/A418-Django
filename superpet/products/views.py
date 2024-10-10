from django.shortcuts import render

# Create your views here.

def products(request):
    return render(request,"products.html")

def royalCanin(request):
    return render(request,"products.html")