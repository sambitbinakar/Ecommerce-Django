from django.shortcuts import render 
from store import models as store_model
# Create your views here.

def home(request):
    feature_products =store_model.Product.objects.filter(features=True)
    catagory = store_model.Category.objects.all()

    context={
        "feature_products":feature_products,
        "catagory":catagory,
    }
    return render(request,'store/homepage.html',context)

def product_page(request):
    product = store_model.Product.objects.all()
    return render(request,'store/product.html',{"product":product})
