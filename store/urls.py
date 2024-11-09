from django.urls import path
from store import views as storeview

urlpatterns=[
    path("",storeview.home,name="homepage"),
]