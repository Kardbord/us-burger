from django.db import models


class SupplyItem(models.Model):
    # TODO: Register this in the database, make the migrations, and start playing with the API and admin side to test.
    """
    SupplyItem class/Model:
    ===================================
    Contains the following members/fields:
    - name: CharField containing the name of the item.
    - units: CharField with the name of the units this item is measured in, i.e. oz, c, gal, box, etc...
    - quantity: FloatField containing the amount of units left in stock.
    """

    def __str__(self):
        """Returns the name of the SupplyItem."""
        return self.name

    def decrement(self, amt):
        """
        Method that's called when a MenuItem requiring this Supply is called.
        If there is sufficient quantity then it decrements, otherwise it raises a descriptive error.
        """
        if amt >= self.quantity:
            self.quantity -= amt
        else:
            raise ValueError("Insufficient quantity of %s.\n\t Need: %s %s, Have: %s %s"
                             % (self.name, str(amt), self.units, str(self.quantity), self.units))

    # member variables
    name = models.CharField(max_length=30)
    units = models.CharField(max_length=10)
    quantity = models.FloatField()


class MenuItem(models.Model):
    """
    MenuItem class/model:
    ===================================
    Contains the following members/fields:
     - available: True or False, depending on if all necessary Inventory items are available.
     - name: CharField containing the name of the dish.
     - ingredients: ManyToManyField relationship that links each MenuItem with the corresponding Inventory items.
     - price: a DecimalField that holds the dish's price, fixed at two decimal places.
     - description: TextField for containing a short description of the dish.
     - image: An ImageField for storing an image of the dish.
        (NOTE): Inherits from FileField, which has some nuances in the documentation that I need to research before
        implementing.
     - orderitem_set : the set of OrderItems that this MenuItem is a part of
    """

    def __str__(self):
        """Returns a formatted string containing the name, price, and description of the item."""
        return "%s - $%s \n\t%s" % (self.name, str(self.price), self.description)

    # TODO: Implement some try-catch functionality for trying to prepare something that's unavailable
    def prepare_item(self):
        pass
        # for supply in supplies try/catch supply.decrement

    def set_quantities(self):
        pass

    available = models.BooleanField(True)
    name = models.CharField(max_length=30)
    # TODO: Figure out how to properly store the SupplyItems along with the quantity for each item.
    #  Maybe create a KeyVal class as the following stackoverflow suggests?
    #  https://stackoverflow.com/questions/402217/how-to-store-a-dictionary-on-a-django-model
    ingredients = models.ManyToManyField(SupplyItem)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    # Next Sprint: Read the documentation and figure out how the ImageField works.
    # image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=100)


class Order(models.Model):
    """
    Order class/model:
    ===================================
    Contains the following members/fields:
    - pin           : a unique PIN number associated with this Order
    - orderitem_set : the set of OrderItems belonging to this Order
    """

    pin = models.PositiveSmallIntegerField(default=0000)

    def __str__(self):
        """Returns the Order's PIN"""
        return str(self.pin)

    def get_total_price(self):
        """Returns the total price of the Order"""
        total = 0.00
        for order_item in self.orderitem_set.all():
            total += order_item.price * order_item.quantity
        return total


class OrderItem(models.Model):
    """
    OrderItem class/model:
    ===================================
    Contains the following members/fields:
     - menu_item : The MenuItem associated with this OrderItem
     - order     : The Order to which this OrderItem belongs
     - quantity  : The quantity of @menu_item ordered
    """

    # A MenuItem can be included in many OrderItems, but an OrderItem can only have one MenuItem
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)

    # An Order can have many OrderItems, but an OrderItem can belong to only one Order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    quantity = models.PositiveSmallIntegerField()

    def __str__(self):
        """Returns the OrderItem's menu_item name"""
        return self.menu_item.name


# TODO: Implement the Menu class/model
class Menu(models.Model):
    pass
