from django.urls import path
from store import views as storeview

app_name='store'

urlpatterns=[
    path("",storeview.home,name="homepage"),
    path("products/<slug:category_slug>",storeview.product_page,name="products"),
    path("detail/<slug>/",storeview.product_detail,name="products_detail"),
    path("add_to_cart/",storeview.add_to_cart,name="add_to_cart"),
]