from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import MenuItem, WaitTime


def index(request):
    wait_time = WaitTime.objects.last()
    context = {
        'wait_time': wait_time
    }
    return render(request, 'restaurant/index.html', context)


def customerMenu(request):
    wait_time = WaitTime.objects.last()
    latest_menu = MenuItem.objects.filter(available=True)
    template = loader.get_template('restaurant/customerMenu.html')
    context = {
        'latest_menu': latest_menu,
        'wait_time': wait_time
    }
    return HttpResponse(template.render(context, request))


def customerOrder(request):
    wait_time = WaitTime.objects.last()
    context = {
        'wait_time': wait_time
    }
    return render(request, 'restaurant/customerOrder.html', context)
