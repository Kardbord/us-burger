from django.shortcuts import render, HttpResponse

from .models import MenuItem

def index(request):
    return render(request, 'restaurant/index.html')

def customerMenu(request):
    return render(request, 'restaurant/customerMenu.html')

def customerOrder(request):
    return render(request, 'restaurant/customerOrder.html')
