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
# TODO: write docstring

    # ------------------------------ Private Attributes -------------------------------- #

    __qty

    __name

    __item

    # ---------------------------- Public Member Functions ----------------------------- #

    def __init__(self, item, qty):
        # TODO: add docstring
        if qty > 0:
            self.__qty = qty
        else:
            self.__qty = 1

        self.__item = item
        try:
            self.__name = self.__item.getName()
        except AttributeError:
            raise AttributeError\
            ('bad "item" passed to OrderItem initializer')
