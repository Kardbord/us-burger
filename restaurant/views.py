from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import MenuItem, WaitTime, Order, OrderItem


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


def newOrder(request):
    # First we need to create a new Order
    # Try to get the Email and the Name from the request.
    try:
        new_order = Order(
            email=request.POST['email'],
            name=request.POST['orderName']
        )
        new_order.save()
    except KeyError:
        return HttpResponse("Could not find email or name.")

    # Then we need to create an OrderItem for each nonzero value in the request
    available_items = MenuItem.objects.filter(available=True)
    for item in available_items:
        item_key = str(item.id) + "qty"
        try:
            item_amt = int(request.POST[item_key])
            if item_amt > 0:
                new_order_item = OrderItem(
                    order=new_order,
                    menu_item=item,
                    quantity=item_amt
                )
                new_order_item.save()
        except KeyError:
            new_order.delete()
            return HttpResponse("Invalid key: %s" % item_key)

    # Finally, save the Order.
    new_order.save()
    return HttpResponseRedirect(reverse('restaurant:customerOrder', kwargs={'order_pk': new_order.pk}))


def customerOrder(request, order_pk):
    wait_time = WaitTime.objects.last()
    order = get_object_or_404(Order, pk=int(order_pk))
    context = {
        'order': order,
        'wait_time': wait_time
    }
    return render(request, 'restaurant/customerOrder.html', context)
