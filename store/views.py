from django.shortcuts import render 

# Create your views here.

def home(request):
    return render(request,'store/homepage.html')
def navbar(request):
    return render(request,'store/navbar.html')