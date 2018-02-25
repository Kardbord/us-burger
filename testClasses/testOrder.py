#!/bin/python

from testMenuItem import MenuItem

class Order:
# TODO: Write docstring

    def __init__(self, pin, items = []):
        """
        Initializer for Order objects

        param pin   : the unique customer PIN associated with this order
        param items : a list of MenuItem objects to be included in the order

        """
        self.__order_items = {}
        self.__total_cost = 0
        self.__pin = ''

        self.__pin = pin
        self.__total_cost = 0.00
        for item in items:

            try:
                self.__total_cost += float(item.getPrice())

                if self.__order_items.has_key(item.getName()):
                    # Increment quantity of an OrderItem if duplicate items are present in the list
                    self.__order_items[item.getName()].incrementQty()
                else:
                    # Add a new OrderItem to self.__order_items
                    order_item = OrderItem(item)
                    self.__order_items.update( {order_item.getName() : order_item} )

            except AttributeError:
                raise AttributeError\
                ('Non-MenuItem object present in Order initializer parameter "items"')


    def getPin(self):
        return self.__pin

    def getCost(self):
        return self.__total_cost

    def getItems(self):
        return self.__order_items


class OrderItem:
    """
    The Order class is composed of OrderItems
    
    Instance Attributes:
        __item: the MenuItem object that was ordered
        __name: the name of the MenuItem object that was ordered
        __qty : the quantity of the MenuItem object that was ordered
    
    """

    def __init__(self, menu_item, qty=1):
        """
        Initializer for OrderItem objects

        param menu_item : a MenuItem object
        param qty       : the quantity of @menu_item ordered

        """
        self.__qty = 1

        self.__name = ''

        if qty > 0:
            self.__qty = qty
        else:
            self.__qty = 1

        self.__item = menu_item
        try:
            self.__name = self.__item.getName()
        except AttributeError:
            raise AttributeError\
            ('bad "menu_item" passed to OrderItem initializer')

    def incrementQty(self):
        self.__qty += 1

    def decrementQty(self):
        if self.__qty > 1:
            self.__qty -= 1

    def updateQuantity(self, qty):
        if qty > 0:
            self.__qty = qty

    def getQuantity(self):
        return self.__qty

    def getName(self):
        return self.__name

    def getItem(self):
        return self.__item

