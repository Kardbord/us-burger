#!/bin/python

""" This file is the work of Tanner Kvarfordt """

from testMenuItem import MenuItem

class Order:
    """
    A composition of OrderItems.

    Instance Attributes:
        __pin         : The unique customer PIN associated with this Order (a string)
        __order_items : A dictionary where
                            key   : name (a string) of OrderItem instance 
                            value : OrderItem instance
        __total_cost  : The total cost of the Order
    
    """

    def __init__(self, pin, items = []):
        """
        Initializer for Order objects

        param pin   : the unique customer PIN associated with this Order
        param items : a list of MenuItem objects to be included in the Order

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

    def updateItemQty(self, item_name, qty):
        """Uses @qty to update the quantity of an OrderItem identified by @item_name"""
        if self.__order_items.has_key(item_name):
            self.__order_items[item_name].updateQuantity(qty)

    def addItem(self, item, qty=1):
        """
        Increases the quantity of @item in self.__order_items by @qty 
        if the item is already included in the Order.
        Inserts @item into the Order with the provided @qty if @item is not already present.
        """
        if self.__order_items.has_key(item.getName()):
            self.__order_items[item.getName()].incrementQty(qty)
        else:
            order_item = OrderItem(item)
            self.__order_items.update( {order_item.getName() : order_item} )
            self.__order_items[order_item.getName()].updateQty(qty)

    def removeItem(self, item_name, qty=1):
        """
        Decreases the quantity of self.__order_items[item_name] by qty 
        if the item is present in the Order.
        If @qty exceeds the present quantity of the OrderItem,
        the OrderItem is removed from the Order entirely.
        """
        if self.__order_items.has_key(item_name):
            order_item = self.__order_items[item_name]
            if order_item.getQuantity() > qty:
                self.__order_items[item_name].decrementQty(qty)
            else:
                del self.__order_items[item_name]

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

    def incrementQty(self, inc_by=1):
        if inc_by > 0:
            self.__qty += inc_by 

    def decrementQty(self, dec_by=1):
        if self.__qty - dec_by > 0 and dec_by > 0:
            self.__qty -= dec_by 

    def updateQty(self, qty):
        if qty > 0:
            self.__qty = qty

    def getQuantity(self):
        return self.__qty

    def getName(self):
        return self.__name

    def getMenuItem(self):
        return self.__item

