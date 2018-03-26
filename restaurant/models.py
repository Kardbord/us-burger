from django.db import models


class WaitTime(models.Model):
    """
    WaitTime class/Model:
    ===================================
    Contains the following members/fields:
    = wait_time : CharField representing the number of minutes customers will have to wait to be sat/get their food
    """

    wait_time = models.CharField(default="0", max_length=4)

    def get_wait_time(self):
        """Returns the wait time"""
        return self.wait_time

    def __str__(self):
        """Returns the wait time and a string indicating that the time is given in minutes"""
        return self.get_wait_time() + " minute wait"


class SupplyItem(models.Model):
    """
    SupplyItem class/Model:
    ===================================
    Contains the following members/fields:
    - name: CharField containing the name of the item.
    - units: CharField with the name of the units this item is measured in, i.e. oz, c, gal, box, etc...
    - quantity: FloatField containing the amount of units left in stock.
    """

    name = models.CharField(max_length=30)
    units = models.CharField(max_length=10)
    quantity = models.FloatField()

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
            self.save()
        else:
            raise ValueError("Insufficient quantity of %s.\n\t Need: %s %s, Have: %s %s"
                             % (self.name, str(amt), self.units, str(self.quantity), self.units))

    def check_availability(self, amt):
        """Method that returns True or False depending on if the supply quantity is sufficient (>= amt)."""
        return self.quantity > amt

    def replenish(self, amt):
        """
        Method that increments the quantity by number value 'amt'. This is used mostly for debugging purposes,
        and may or may not be used further into production."""
        self.quantity += amt
        self.save()


class SupplyAmt(models.Model):
    """
    SupplyItem class/model:
    ==============================
    SupplyAmt behaves as a very detailed key-value pair that allows each MenuItem to list the quantity it needs for each
    of its ingredients, which its associated to indirectly through one SupplyAmt for each SupplyItem. By using this we
    eliminate the need for the SupplyItem itself to know how much of itself is required for each MenuItem.
    SupplyAmt contains the following members/Fields:
     - supply: each SupplyAmt is connected to exactly one SupplyItem via ForeignKey in this data member.
     - item: each SupplyAmt is connected to exactly one MenuItem via ForeignKey.
     - amt: the quantity of SupplyItem that the associated MenuItem requires.
    One advantage of using this ForeignKey setup is that even though SupplyItems don't NEED to know which MenuItem
    recipes they're a part of, we can easily implement that functionality at a later date by using self.supplyamt_set
    in SupplyItem the way we do in MenuItem.
    """
    supply = models.ForeignKey('SupplyItem', on_delete=models.PROTECT)
    item = models.ForeignKey('MenuItem', on_delete=models.CASCADE)
    amt = models.IntegerField()

    def __str__(self):
        """Concatenates and lightly formats the names of the associated MenuItem and SupplyItem and the amt."""
        return self.item.name + ": " + self.supply.name + "\n" + str(self.amt) + " " + self.supply.units

    def decrement(self):
        """
        Method that is called from the 'parent' MenuItem that in turn calls the decrement function in the
        associated SupplyItem.
        """
        self.supply.decrement(self.amt)

    def check_availability(self):
        """Method that returns the availability of the associated SupplyItem."""
        return self.supply.check_availability(self.amt)

    def replenish(self, amt):
        """Increments the associated SupplyItem's quantity by an amt passed to this by the associated MenuItem."""
        self.supply.replenish(amt)


class MenuItem(models.Model):
    """
    MenuItem class/model:
    ===================================
    Contains the following members/fields:
     - available: True or False, depending on if all necessary Inventory items are available.
     - name: CharField containing the name of the dish.
     - price: a DecimalField that holds the dish's price, fixed at two decimal places.
     - description: TextField for containing a short description of the dish.
     - orderitem_set : the set of OrderItems that this MenuItem is a part of
     - menu_set : the set of Menus that this MenuItem is a part of
     - supplyamt_set: the set of SupplyAmt's that 'belong' to this MenuItem.
    """

    available = models.BooleanField(True)
    name = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        """Returns a formatted string containing the name, price, and description of the item."""
        self.check_availability()
        return "%s - $%s" % (self.name, str(self.price))

    def replenish(self, amt):
        """Method that increments each associated SupplyItem's quantity by amt, then updates availability."""
        for supply in self.supplyamt_set.all():
            supply.replenish(amt)
        self.check_availability()
        self.save()

    def prepare_item(self):
        """
        Method that first checks the availability of the MenuItem by checking each of its associated SupplyItems,
        then decrements each SupplyItem, saving once it's all done.
        """
        self.check_availability()
        if self.available is True:
            print("Available!")
            for supply in self.supplyamt_set.all():
                try:
                    supply.decrement()
                except ValueError as err:
                    print(err[0])
            self.save()
        else:
            print("Unavailable!")

    def print_ingredients(self):
        """
        Method used for debugging before I got everything working on the admin/HTML side. Likely won't be
        used in production.
        """
        print("Ingredients for " + self.name)
        for supply in self.supplyamt_set.get_queryset():
            print(supply)

    def check_availability(self):
        """
        This method will check all the SupplyItems and make sure that there is enough inventory
        to create at least one of these MenuItems. Later, we can also add time checking for lunch/
        breakfast etc...
        """
        for supply in self.supplyamt_set.all():
            if not supply.check_availability():
                self.available = False
                self.save()
                return
        # After you make it through all of the ingredients, set availability to True
        self.available = True
        self.save()


class Order(models.Model):
    """
    Order class/model:
    ===================================
    Contains the following members/fields:
     - pin                       : a unique PIN number associated with this Order
     - orderitem_set             : the set of OrderItems belonging to this Order
     - order_items_are_available : boolean indicating whether or not each OrderItem is in stock and the Order
                                   can be placed.
                                   Initialized to False. check_availability function must be run to verify
    """

    pin = models.CharField(max_length=4, default=0000)

    order_items_are_available = models.BooleanField(default=False)

    comfirmed = models.BooleanField(default=False)
    cooking = models.BooleanField(default=False)
    cooked = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    def __str__(self):
        """Returns the Order's PIN"""
        return str(self.pin)

    def check_availability(self):
        """
        Verifies all OrderItems are in stock.
        Sets order_items_are_available field to True if all OrderItems are in stock and Order can be placed.
        Sets order_items_are_available field to False if an OrderItem is out of stock and Order cannot be placed.
        """
        for order_item in self.orderitem_set.all():
            if not order_item.check_availability():
                self.order_items_are_available = False
                self.save()
                return
        self.order_items_are_available = True
        self.save()

    def get_total_price(self):
        """Returns the total price of the Order"""
        total = 0.00
        for order_item in self.orderitem_set.all():
            total += float(order_item.get_price() * order_item.quantity)
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

    def get_price(self):
        return self.menu_item.price

    def check_availability(self):
        """Returns true if all needed ingredients are present. Returns false otherwise."""
        self.menu_item.check_availability()
        return self.menu_item.available

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
