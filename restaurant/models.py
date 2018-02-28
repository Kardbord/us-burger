from django.db import models

# TODO: Register this in the database, make the migrations, and start playing with the API and admin side to test.
"""
SupplyItem class/Model:
===================================
Contains the following members/fields:
 - name: CharField containing the name of the item.
 - units: CharField with the name of the units this item is measured in, i.e. oz, c, gal, box, etc...
 - quantity: FloatField containing the amount of units left in stock.
"""


class SupplyItem(models.Model):

    """Returns the name of the SupplyItem."""
    def __str__(self):
        return self.name

    """
    Method that's called when a MenuItem requiring this Supply is called.
    If there is sufficient quantity then it decrements, otherwise it raises a descriptive error.
    """
    def decrement(self, amt):
        if amt <= self.quantity:
            self.quantity -= amt
        else:
            raise ValueError("Insufficient quantity of %s.\n\t Need: %s %s, Have: %s %s"
                             % (self.name, str(amt), self.units, str(self.quantity), self.units))

    # member variables
    name = models.CharField(max_length=30)
    units = models.CharField(max_length=10)
    quantity = models.FloatField()


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
    (NOTE): Inherits from FileField, which has some nuances in the documentation that I need to research before implementing.
 - 
"""


class MenuItem(models.Model):

    """Returns a formatted string containing the name, price, and description of the item."""
    def __str__(self):
        return "%s - $%s \n\t%s" %(self.name, str(self.price), self.description)

    """Method that should be called for each MenuItem upon submission of an Order."""
    def prepare_item(self):
        # First make sure each ingredient has an amount defined in ingredients_amt
        '''
        for supply in self.ingredients.all():
            if self.ingredients_amt[supply.name] is None:
                print("No quantity for SupplyItem: %s set for %s" % (supply.name, self.name))
                return
        '''
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


# TODO: Implement the Menu class/model
class Menu(models.Model):
    pass


# TODO: Implement the Order class/model
class Order(models.Model):
    pass
