#Sprint 1: Testing MenuItems
The following steps and shell code outline the steps necessary to change the database values 
    through method calls, and then see those changes reflected on the website.
    
1. Perform a git pull to ensure that you have the most recent `db.sqlite` file that has all of the
    MenuItems, SupplyItems and SupplyAmts created. (Note: I had to delete my local db.sqlite3 file in 
    order to do this.) Once you've pulled, you'll probably have to create a new SuperUser, but after you've
    done that you should be able to access all of the admin stuff as normal, just with the same database
    entries that everyone else is using.
2. Once all that git stuff is out of the way, you can `$python manage.py runserver` and then go to
    [localhost:8000/admin](localhost:8000/admin) to login, and view and change the database entries.
3. After you've made sure there is valid data, go to [localhost:8000/restaurant/customerMenu/](
    localhost:8000/restaurant/customerMenu/) to view the menu. If you've followed up to this point and
    are using our 'standardized' menu, you should see an entry for each of the 6 current MenuItems.
4. Now, go back to your IDE and enter the python shell (`$python manage.py shell` if you forgot)
5. Follow along with this Python code:
  ```
    >>>from restaurant.models import *
    >>>m = MenuItem.objects.filter(pk=1)[0]
    >>>m
    <MenuItem: Cheeseburger - $6.00>
    >>>while m.available:
    ...     m.prepare_item()
    ...     
    >>>Available! #This will print out a few times depending on the exact quantities of your SupplyItems
    >>>quit()
  ```
Now, if you refresh the CustomerMenu page, you should no longer see the Cheeseburger! Note: if the while
    loop doesn't print out "Available", that means you're out of one of the necessary SupplyItems. Call
    `m.replenish(10)` to increment each of the supply quantities by 10, then try calling `m.prepare_item()`
    