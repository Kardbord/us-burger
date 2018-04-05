import os
import django
from restaurant.models import *
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'us_burger.settings')

django.setup()


def populate():
    """
    Removes all entries in the database, then repopulates the SupplyAmts, SupplyItems, MenuItems, Menus, and WaitTime
    """

    Order.objects.all().delete()
    Host.objects.all().delete()
    OrderItem.objects.all().delete()
    MenuItem.objects.all().delete()
    Menu.objects.all().delete()
    SupplyItem.objects.all().delete()
    SupplyAmt.objects.all().delete()
    WaitTime.objects.all().delete()

    # Create WaitTime
    wait = WaitTime(wait_time=0)
    wait.save()

    # Create SupplyItems
    tomato_soup = SupplyItem(name='Tomato Soup', units='oz', quantity=10)
    tomato_soup.save()

    sliced_potato = SupplyItem(name='Sliced Potato', units='oz', quantity=10)
    sliced_potato.save()

    sliced_chicken = SupplyItem(name='Sliced Chicken', units='oz', quantity=10)
    sliced_chicken.save()

    cheese = SupplyItem(name='Cheese', units='oz', quantity=10)
    cheese.save()

    bread = SupplyItem(name='bread', units='oz', quantity=10)
    bread.save()

    lettuce = SupplyItem(name='Lettuce', units='oz', quantity=10)
    lettuce.save()

    burger_patty = SupplyItem(name='Burger Patty', units='oz', quantity=10)
    burger_patty.save()

    burger_bun = SupplyItem(name='Burger Bun', units='oz', quantity=10)
    burger_bun.save()

    # Create MenuItems
    tom_soup = MenuItem(name='Tomato Soup', price=4, description='Great with grilled cheese!', available=False)
    tom_soup.save()
    supply_amt1 = SupplyAmt(item=tom_soup, supply=tomato_soup, amt=5)
    supply_amt1.save()
    tom_soup.supplyamt_set.add(supply_amt1)
    tom_soup.check_availability()
    tom_soup.save()

    gril_cheese = MenuItem(name='Grilled Cheese', price=4, description='Great with tomato soup!', available=False)
    gril_cheese.save()
    supply_amt1 = SupplyAmt(item=gril_cheese, supply=cheese, amt=2)
    supply_amt2 = SupplyAmt(item=gril_cheese, supply=bread, amt=2)
    supply_amt1.save()
    supply_amt2.save()
    gril_cheese.supplyamt_set.add(supply_amt1, supply_amt2)
    gril_cheese.check_availability()
    gril_cheese.save()

    chick_salad = MenuItem(name='Chicken Salad', price=8, description='Freshly chopped lettuce and delicious chicken!',
                           available=False)
    chick_salad.save()
    supply_amt1 = SupplyAmt(item=chick_salad, supply=lettuce, amt=5)
    supply_amt2 = SupplyAmt(item=chick_salad, supply=sliced_chicken, amt=2)
    supply_amt1.save()
    supply_amt2.save()
    chick_salad.supplyamt_set.add(supply_amt1, supply_amt2)
    chick_salad.check_availability()
    chick_salad.save()

    fries = MenuItem(name='Fries', price=2, description='Salty and delicious!', available=False)
    fries.save()
    supply_amt1 = SupplyAmt(item=fries, supply=sliced_potato, amt=3)
    supply_amt1.save()
    fries.supplyamt_set.add(supply_amt1)
    fries.check_availability()
    fries.save()

    burger = MenuItem(name='Cheeseburger', price=6, description='Our cheese is mostly fresh!', available=False)
    burger.save()
    supply_amt1 = SupplyAmt(item=burger, supply=burger_patty, amt=1)
    supply_amt2 = SupplyAmt(item=burger, supply=burger_bun, amt=1)
    supply_amt1.save()
    supply_amt2.save()
    burger.supplyamt_set.add(supply_amt1, supply_amt2)
    burger.check_availability()
    burger.save()

    # Create Menu
    lunch = Menu(name='Lunch Menu')
    lunch.save()
    lunch.menu_items.add(tom_soup, gril_cheese, chick_salad)
    lunch.save()

    dinner = Menu(name='Dinner Menu')
    dinner.save()
    dinner.menu_items.add(tom_soup, gril_cheese, chick_salad, fries, burger)
    dinner.save()

    # Create some Orders
    order = Order(pin='0001', email='email@email.com', name='order1')
    order2 = Order()
    order3 = Order(pin='1112', email='johndoe@www.com', name='John\'s order')
    order.save()
    order2.save()
    order3.save()

    # Create some OrderItems for the Orders
    fry_item = OrderItem(menu_item=fries, order=order, quantity=3)
    fry_item.save()
    burger_item = OrderItem(menu_item=burger, order=order, quantity=1)
    burger_item.save()
    soup_item = OrderItem(menu_item=tom_soup, order=order2, quantity=1)
    soup_item.save()
    gril_cheese_item = OrderItem(menu_item=gril_cheese, order=order2, quantity=2)
    gril_cheese_item.save()
    salad_item = OrderItem(menu_item=chick_salad, order=order3, quantity=4)
    salad_item.save()

    order.check_availability()
    order.save()
    order2.check_availability()
    order2.save()
    order3.check_availability()
    order3.save()

    # Create some Hosts
    # TODO: Figure out why this gives the same PIN to the 4 Hosts created in populate()
    host1 = Host(name='Samantha')
    host2 = Host(name='Jonathan')
    host3 = Host(name='Eliza')
    host4 = Host(name='Peter')
    host1.save()
    host2.save()
    host3.save()
    host4.save()


if __name__ == '__main__':
    populate()
