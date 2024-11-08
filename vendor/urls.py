from django.urls import path
from vendor import views as vendor_view


urlpatterns=[
    path("",vendor_view.index)
]