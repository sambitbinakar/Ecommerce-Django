from decimal import Decimal
from django.shortcuts import render ,get_object_or_404
from store import models as store_model
from store.models import * 
from django.http import JsonResponse
from django.db.models import Q,Avg,Sum

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
    related_product = store_model.Product.objects.filter(category=product.category,status="published",features=True).exclude(id=product.id)
    product_stock_range = range(1,product.stock+1)
    context ={
        "product":product,
        "related_product":related_product,
        "product_stock_range":product_stock_range
    }
    return render(request,'store/product_detail.html',context)

def add_to_cart(request):
    id = request.GET.get('id')
    qty = request.GET.get('qty')
    color = request.GET.get('color')
    size = request.GET.get('size')
    cart_id = request.GET.get('cart_id')

    request.session['cart_id'] = cart_id

    if not id or not qty or not cart_id:
        return JsonResponse({"error": "No id ,qty or cart_id"},status=400)
    try:
        product = store_model.Product.objects.get(status="published", id=id)
    except store_model.Product.DoesNotExist:
        return JsonResponse({"error":"product not found"}, status = 404)
    
    existing_cart_item = store_model.Cart.objects.filter(cart_id=cart_id, product=product).first()
    if int(qty) > product.stock:
        return JsonResponse({"error":'Qty exceed current stock amount'}, status=404)
    
    if not existing_cart_item:
        cart = store_model.Cart()
        cart.product = product
        cart.qty = qty
        cart.price = product.price
        cart.color = color
        cart.size = size
        cart.sub_total = Decimal(product.price)* Decimal(qty)
        cart.shipping =  Decimal(product.shipping)* Decimal(qty)
        cart.total = cart.sub_total * cart.shipping
        cart.user = request.user if request.user.is_authenticated else None
        cart.cart_id = cart_id
        cart.save()

        message = "Item added to cart"
    else:
        existing_cart_item = store_model.Cart()
        existing_cart_item.product = product
        existing_cart_item.qty = qty
        existing_cart_item.price = product.price
        existing_cart_item.color = color
        existing_cart_item.size = size
        existing_cart_item.sub_total = Decimal(product.price)* Decimal(qty)
        existing_cart_item.shipping =  Decimal(product.shipping)* Decimal(qty)
        existing_cart_item.total = existing_cart_item.sub_total * existing_cart_item.shipping
        existing_cart_item.user = request.user if request.user.is_authenticated else None
        existing_cart_item.cart_id = cart_id
        existing_cart_item.save()

        message ="Cart updated"
    
    total_cart_items = store_model.Cart.objects.filter(Q(cart_id=cart_id) | Q(cart_id=cart_id))
    cart_sub_total = store_model.Cart.objects.filter(Q(cart_id=cart_id) | Q(cart_id=cart_id)).aggregate(sub_total= Sum("sub_total")['sub_total'])

    return JsonResponse({
        'message':message ,
        "total_cart_items":total_cart_items.count(),
        "cart_sub_total":"{:,.2f}".format(cart_sub_total),
        "item_sub_total":"{:,.2f}".format(existing_cart_item.sub_total) if existing_cart_item else "{:,.2f}".format(cart.cart_sub_total) ,
    })

