from typing import Any
from django.shortcuts import render
from .models  import Product,Category
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required


def products(request):
    return render(request,"products.html")

def royalCanin(request):
    products=Product.customManager.royalCanin()

    return render(request,"products.html",{"products":products})

def search(request):
    keyword=request.GET.get("keyword")
    products=Product.customManager.all().filter(product_name__icontains=keyword)
    return render(request,"products.html",{"products":products})

class ProductListView(ListView):
    model=Product

class ProductDetailView(DetailView):
    # product
    model=Product   
    template_name="products/productdetail.html"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["products"]=Product.customManager.all()
        # context["name"]="Priyanka"
        return context



@method_decorator(staff_member_required,name="dispatch")
class ProductCreateView(CreateView):
    model=Product
    fields="__all__"
    success_url="/products"

@method_decorator(staff_member_required,name="dispatch")
class ProductUpdateView(UpdateView):
    model=Product
    fields="__all__"
    success_url="/products"
    
@method_decorator(staff_member_required,name="dispatch")
class ProductDeleteView(DeleteView):
    model=Product
    success_url="/products"


# --------------------------------------------------

class CategoryDetailView(DetailView):
    model=Category
    template_name="category/category_detail.html"
    slug_field="category_slug"
    context_object_name="category_obj"

    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context["categories"]=Category.objects.all()
        return context

    