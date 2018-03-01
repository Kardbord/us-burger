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
        if amt <= self.quantity:
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
     - menu_set : the set of Menus that this MenuItem is a part of
    """

    def __str__(self):
        """Returns a formatted string containing the name, price, and description of the item."""
        return "%s - $%s \n\t%s" % (self.name, str(self.price), self.description)

    """Method that should be called for each MenuItem upon submission of an Order."""
    def prepare_item(self):
        # First make sure each ingredient has an amount defined in ingredients_amt
        """
        for supply in self.ingredients.all():
            if self.ingredients_amt[supply.name] is None:
                print("No quantity for SupplyItem: %s set for %s" % (supply.name, self.name))
                return
        """
        # Now decrement quantity in each supply.
        for supply in self.ingredients.all():
            # amt = self.ingredients_amt[supply.name]
            try:
                amt = self.ingredients_amt[supply.name]
                supply.decrement(amt)
            except KeyError as err:
                print("No quantity for SupplyItem: %s set for %s" % (err.args[0], self.name))
                return
            except ValueError as err:
                print(err.args[0])
                return
        print("Enjoy your yummy %s!" % self.name)

    """Method that should be called in the API before Orders can be created."""
    def set_quantity(self, item, amt):
        i = self.ingredients.filter(name=item)
        if len(i) == 1:
            self.ingredients_amt[item] = amt
        else:
            print("Could not find SupplyItem: %s in %s's ingredients." % (item, self.name))

    available = models.BooleanField(True)
    name = models.CharField(max_length=30)
    ingredients = models.ManyToManyField(SupplyItem)
    ingredients_amt = {}
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()


class Order(models.Model):
    """
    Order class/model:
    ===================================
    Contains the following members/fields:
     - pin           : a unique PIN number associated with this Order
     - orderitem_set : the set of OrderItems belonging to this Order
    """

    pin = models.CharField(max_length=4, default=0000)

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


class Menu(models.Model):
    """
    Menu class/model:
    ===================================
    Contains the following members/fields:
     - name       : the name of the Menu
     - menu_items : the MenuItems included in the Menu
    """

    name = models.CharField(max_length=200, default="Menu")

    # MenuItems can be on multiple Menus, and Menus are made up of multiple MenuItems
    menu_items = models.ManyToManyField(MenuItem)

    def __str__(self):
        """Returns the Menu's name"""
        return self.name
