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


    # ---------------------------- Private Member Functions ---------------------------- #

