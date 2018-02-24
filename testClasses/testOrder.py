from testMenuItem import MenuItem

class Order:
# TODO: Write docstring

    # ------------------------------ Private Attributes -------------------------------- #
    __items

    __total_cost

    __pin

    # ---------------------------- Public Member Functions ----------------------------- #
    def __init__(self, pin, items = []):
        self.__pin = pin
        self.__total_cost = 0.00
        self.__items = items
        for item in self.__items:
            self.__total_cost += item.getPrice()

    def getPin(self):
        return self.__pin

    def getCost(self):
        return self.__total_cost

    def getItems(self):
        return self.__items



class OrderItem:
"""
The Order class is composed of OrderItems

Attributes:
    __item: the MenuItem object that was ordered
    __name: the name of the MenuItem object that was ordered
    __qty : the quantity of the MenuItem object that was ordered

"""
    # ------------------------------ Private Attributes -------------------------------- #

    __qty

    __name

    __item

    # ---------------------------- Public Member Functions ----------------------------- #

    def __init__(self, menu_item, qty):
        """
        Initializer for OrderItem objects

        param menu_item : a MenuItem object
        param qty       : the quantity of @menu_item ordered

        """
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

    def getQuantity(self):
        return self.__qty

    def getName(self):
        return self.__name

    def getItem(self):
        return self.__item
