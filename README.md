# Us Burger README

##Testing MenuItem/SupplyItem

First make sure you've followed the Django steps to create a superuser in the admin side, 
perform initial migrations for MenuItem and SupplyItem, and then registered them (the registering
should already be done in our shared restaurant/admin.py file). Once you've created a few MenuItems 
and their corresponding SupplyItems on the admin page (I use the ones Gavin made in his recipes.txt), 
you'll need to set a quantity for each SupplyItem using the API from the Python Shell. To do so, 
follow these commands:

```
$ python manage.py shell
>>>from restaurant.models import MenuItem, SupplyItem
>>>m = MenuItem.objects.filter(pk=1)[0]
>>>m
<MenuItem: Cheeseburger - $6.00
    A hamburger topped with cheese so good it will leave your tastebuds wanting more!>
>>>m.ingredients.all()
<QuerySet [<SupplyItem: bun>, <SupplyItem: hamburger>, <SupplyItem: cheese>, 
    <SupplyItem: lettuce>, <SupplyItem: tomato>]>
>>>m.set_quantity("bun", 1)
>>>m.set_quantity("hamburger", 1)
>>>m.set_quantity("cheese", 1)
>>>m.set_quantity("lettuce", 1)
>>>m.set_quantity("tomato", 2)
>>>m.prepare_item()
Enjoy your yummy Cheeseburger!
>>>m.save() #Only call this if you want to save the quantities for the next time you want to test.
```

Obviously, your exact inputs and outputs will differ depending on the specifics of the instances you
create on your Admin page, but the process should be the same. Ideally, we would like a way to change this
on the Admin page, but we can save that for a later sprint.