from django.shortcuts import render ,get_object_or_404
from store import models as store_model
from store.models import * 
# Create your views here.

def home(request):
    feature_products =store_model.Product.objects.filter(features=True)
    catagory = store_model.Category.objects.all()

    context={
        "feature_products":feature_products,
        "catagory":catagory,
    }
    return render(request,'store/homepage.html',context)

def product_page(request,category_slug):
    category= get_object_or_404(Category, slug=category_slug)
    products= store_model.Product.objects.filter(category=category)
    return render(request,'store/product.html',{'category':category,'products':products})



def product_detail(request,slug):
    product = store_model.Product.objects.get(status="published",slug=slug)
    related_product = store_model.Product.objects.filter(category=product.category,status="published").exclude(id=product.id)
    product_stock_range = range(1,product.stock+1)
    context ={
        "product":product,
        "related_product":related_product,
        "product_stock_range":product_stock_range
    }
    return render(request,'store/product_detail.html',context)