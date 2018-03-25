from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404

from .models import MenuItem, WaitTime, Order


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


# TODO: once the customerMenu sends an order_pk, replace function def with the line below
#def customerOrder(request, order_pk):
#    wait_time = WaitTime.objects.last()
#    order = get_object_or_404(Order, pk=order_pk)
#    context = {
#        'order': order,
#        'wait_time': wait_time
#    }
#    return render(request, 'restaurant/customerOrder.html', context)
def customerOrder(request):
    wait_time = WaitTime.objects.last()
    context = {
        'wait_time': wait_time
    }
    return render(request, 'restaurant/customerOrder.html', context)
