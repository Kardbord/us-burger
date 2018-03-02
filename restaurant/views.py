from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import MenuItem


def index(request):
    return render(request, 'restaurant/index.html')

def customerMenu(request):
    latest_menu = MenuItem.objects.filter(available=True)
    template = loader.get_template('restaurant/customerMenu.html')
    context = {
        'latest_menu': latest_menu
    }
    return HttpResponse(template.render(context, request))

def customerOrder(request):
    return render(request, 'restaurant/customerOrder.html')
