from django.shortcuts import render

def home(request):
    
    return render ( request,'rentals/home.html')
