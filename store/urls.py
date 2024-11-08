from django.urls import path
from store import views as storeview

urlpatterns=[
    path("",storeview.home,name="homepage"),
    path("navbar/",storeview.navbar,name="navbar"),
]