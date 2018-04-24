from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.urls import reverse
import json

from populate_database import populate

from .models import MenuItem, WaitTime, Order, OrderItem, Host, Table, SupplyItem


def init(request):
    """
    This view serves as an easy method of repopulating the database.
    It is for testing/developing purposes only, and should ABSOLUTELY NOT be included in the production build.
    """
    populate()
    return HttpResponseRedirect(reverse('restaurant:index'))


def index(request):
    serialize_emails = serializers.serialize("json", Order.objects.all(), indent=4)

    wait_time = WaitTime.objects.last()
    latest_menu = MenuItem.objects.all()
    context = {
        'latest_menu': latest_menu,
        'wait_time': wait_time,
        'emails': serialize_emails
    }
    return render(request, 'restaurant/index.html', context)


def customerMenu(request):
    serialize_emails = serializers.serialize("json", Order.objects.all(), indent=4)

    wait_time = WaitTime.objects.last()
    latest_menu = MenuItem.objects.filter(available=True)
    template = loader.get_template('restaurant/customerMenu.html')
    context = {
        'latest_menu': latest_menu,
        'wait_time': wait_time,
        'emails': serialize_emails
    }
    return HttpResponse(template.render(context, request))


def changeButton(order: int, button: str):
    thisOrder = Order.objects.get(id=order)

    if button == "1":
        if thisOrder.cooking and not thisOrder.cooked:
            thisOrder.cooking = False
            thisOrder.save()
            return False
        else:
            thisOrder.changeCooking()
            thisOrder.save()
            return True


    elif button == "2":
        if thisOrder.cooked and not thisOrder.delivered:
            thisOrder.cooked = False
            thisOrder.save()
            return False
        else:
            thisOrder.changeCooked()
            thisOrder.save()
            return True

    elif button == "3":
        if thisOrder.delivered:
            thisOrder.delivered = False
            thisOrder.save()
            return False
        else:
            thisOrder.changeDelivered()
            thisOrder.save()
            return True

    elif button == "4":
        ran = 4
    # if thisTable.order.cooking:
    #	thisTable.order.cooking = False
    # else:
    #	thisTable.order.cooking.changeCooking()

    elif button == "5":
        ran = 5

    else:
        ran = 3

    return button


def button(request):
    if 'button' in request.GET:
        table = request.GET.get('order')
        button = request.GET.get('button')
        resp = {'answer': changeButton(request.GET.get('order'), request.GET.get('button'))}
    else:
        rep = {'ERROR': "use the HTTP request variable 'n' and 'button"}

    return HttpResponse(json.dumps(resp))


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

    menu_items = MenuItem.objects.all()
    for item in menu_items:
        item_key = str(item.pk) + 'qty'
        try:
            item_amt = int(request.POST[item_key])
            if item_amt > 0:
                item.check_availability(qty=item_amt)
        except KeyError:
            pass

    # Then we need to create an OrderItem for each nonzero value in the request
    item_count = 0
    for item in menu_items:
        item_key = str(item.pk) + "qty"
        try:
            item_amt = int(request.POST[item_key])
            if item_amt > 0:
                item_count += 1
                if item.available:
                    new_order_item = OrderItem(
                        order=new_order,
                        menu_item=item,
                        quantity=item_amt
                    )
                    new_order_item.save()
        except KeyError:
            pass

    new_order.save()

    # Verify that a valid order was placed
    if (not new_order.orderitem_set.exists()) or (item_count != new_order.orderitem_set.count()):
        new_order.delete()
        return HttpResponseRedirect(reverse('restaurant:orderFailed'))

    # Prepare the order
    for item in new_order.orderitem_set.all():
        item.prepare()
    # Finally, save the Order.
    new_order.save()
    for item in MenuItem.objects.all():
        item.check_availability()
    return HttpResponseRedirect(reverse('restaurant:customerOrder', kwargs={'order_pk': new_order.pk}))


def order_failed(request):
    wait_time = WaitTime.objects.last()
    context = {
        'wait_time': wait_time,
    }
    return render(request, 'restaurant/orderFailed.html', context)


def customerOrder(request, order_pk):
    wait_time = WaitTime.objects.last()
    order = get_object_or_404(Order, id=int(order_pk))
    context = {
        'order': order,
        'wait_time': wait_time
    }
    return render(request, 'restaurant/customerOrder.html', context)


def verify(request):
    # order = get_object_or_404(Order, email=request.POST['orderEmail'])
    try:
        order = Order.objects.get(email=request.POST['orderEmail'])
    except (KeyError, Order.DoesNotExist):
        return HttpResponseRedirect(reverse('restaurant:index'), )

    if order.name != request.POST['orderName']:
        return HttpResponseRedirect(reverse('restaurant:index'), )
    # return HttpResponse("This is a new page.")
    return HttpResponseRedirect(reverse('restaurant:customerOrder', args=(order.pk,)))


def confirm(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)

    try:
        table = Table.objects.get(number=request.POST.get('tableNumber'))
        if table.available:
            table.order_set.add(order)
            table.available = False
            table.save()

    except (KeyError, Table.DoesNotExist):
        return HttpResponseRedirect(reverse('restaurant:customerOrder', args=(order.pk,)))

    pin = request.POST.get('serverPin')
    comments = request.POST.get('orderComments', '')

    order.comment = comments

    all_Hosts = Host.objects.all()

    for n in all_Hosts:
        if pin == n.pin:
            order.changeConfirmed()
            order.save()

    return HttpResponseRedirect(reverse('restaurant:customerOrder', args=(order.pk,)))


def server(request):
    wait_time = WaitTime.objects.last()
    tables = Table.objects.all()
    context = {
        'wait_time': wait_time,
        'tableList': tables
    }

    return render(request, 'restaurant/serverPage.html', context)


def delete(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)

    if not order.confirmed:
        for item in order.orderitem_set.all():
            item.replenish()
        order.delete()

    return HttpResponseRedirect(reverse('restaurant:index'), )


def editOrder(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    latest_menu = MenuItem.objects.filter(available=True)
    template = loader.get_template('restaurant/editOrder.html')
    order_qtys = {}
    for item in latest_menu:
        order_qtys[item.name] = order.getValueByName(item.name)
    context = {
        'latest_menu': latest_menu,
        'order': order,
        'order_qtys': order_qtys
    }
    return HttpResponse(template.render(context, request))


def changeOrder(request, order_pk):
    this_order = get_object_or_404(Order, pk=order_pk)
    # delete the existing order items since we want to overwrite them.
    for item in this_order.orderitem_set.all():
        item.delete()

    # create new order_items for each nonzero value in the request
    available_items = MenuItem.objects.filter(available=True)
    for item in available_items:
        item_key = str(item.id) + "qty"
        try:
            item_amt = int(request.POST[item_key])
            if item_amt > 0:
                new_order_item = OrderItem(
                    order=this_order,
                    menu_item=item,
                    quantity=item_amt
                )
                new_order_item.save()
        except KeyError:
            new_order.delete()
            return HttpResponse("Invalid key: %s" % item_key)

    # Finally, save the Order.
    this_order.save()
    return HttpResponseRedirect(reverse('restaurant:customerOrder', kwargs={'order_pk': this_order.pk}))


def employeeLogin(request):
    return render(request, 'restaurant/login.html')


def tryLogin(request):
    try:
        login_name = request.POST['name']
        login_PIN = request.POST['PIN']
        employee = Host.objects.get(name=login_name)
        if employee.checkPin(login_PIN):
            return HttpResponseRedirect(reverse('restaurant:employeePortal'))
        else:
            raise KeyError
    except (KeyError, Host.DoesNotExist):
        return HttpResponse("Invalid Login Credentials")

def employeePortal(request):
    template = loader.get_template('restaurant/employeePortal.html')
    return HttpResponse(template.render({}, request))

def cookOrder(request):
    order_list = Order.objects.all()
    context = {
        'order_list': order_list,
    }
    return render(request, 'restaurant/cookOrder.html', context)


def ingredients(request):
    ingredient_list = SupplyItem.objects.all()
    context = {
        'ingredient_list': ingredient_list,
    }
    return render(request, 'restaurant/ingredients.html', context)
