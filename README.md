# Sprint 2: Creating, Editing, and Deleting Orders
The following steps outline how to navigate the website and view the changes both from the app and on the
admin page.

 1. Perform a git pull to ensure that you have the most recent changes. We're no longer using the same
 `db.sqlite` file, so this shouldn't be as big of an issue as it has been in the past.
 2. Run the following commands from the terminal within the project directory: 
    * `$ python manage.py makemigrations restaurant`
    * `$ python manage.py migrate`
    * `$ python manage.py runserver`
    
    We've found that for some reason, it's necessary to add the 'restaurant' after makemigrations for it
    to correctly apply things. 
 3. Navigate to [localhost:8000/init](localhost:8000/init) to run Tanner K.'s populate method to wipe 
 any local MenuItem entries and populate everything with our 'defaults'.
 
 # Presentation:
Using a narrative involving my wife and I going out to dinner on a Friday night, I will showcase the
functionality of our app by following these steps:
 1. Pull up localhost:8080 to see the home page.
 2. Pull up localhost:8080/admin to view the changes to our database as they happen.
 3. Mention the init functionality.
 4. Note the wait time, defaulting to 0. Change it on the admin side, and then view the change on the page.
 5. Create an Order with 2 Soups, 2 Grilled Cheeses, and 1 Fries with my name and email.
 6. View the Order on the Website, and show it on the Admin page.
 7. Delete the Order. Recreate the Order with 1 less tomato soup, same name and email.
 8. Close the window entirely, navigate back to the home page, and then input name and email to get to Order.
 9. Click the Edit Order, add an additional order of fries, show the change on the admin.
 10. Create a Host named Tanner on the admin side, note his automatically generated PIN.
 11. Use Tanner's PIN to confirm the Order.
 12. Try to change or delete the Order.
 13. The rest is up to the restaurant staff, the user is done giving input for now. 
 14. Change the status of the order on the admin side, note the change on the customer side.