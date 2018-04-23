from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    # ex: /restaurant/
    path('', views.index, name='index'),
    # ex: /restaurant/customerMenu/
    path('customerMenu/', views.customerMenu, name='customerMenu'),
    # Path to newOrder view, which reverses to customerOrder
    path('newOrder/', views.newOrder, name='newOrder'),
    # ex: /restaurant/customerOrder/1
    path('customerOrder/<int:order_pk>/', views.customerOrder, name='customerOrder'),
    # this will verify if an order exists
    path('verify/', views.verify, name='verify'),
    # ex: /init/
    # This url is for testing/developing purposes ONLY
    # TODO: delete this in production version
    path('init/', views.init, name='init'),
    # This url will test the validity of the host pin
    # to change the order status to confirmed.
    path('customerOrder/<int:order_pk>/confirm/', views.confirm, name='confirm'),
    # This url will take you to the edit order page for the corresponding order.
    path('editOrder/<int:order_pk>', views.editOrder, name='editOrder'),
    # This will go to the Server Page.
    path('serverPage/', views.server, name='server'),
    # This will delete the order specified.
    path('customerOrder/<int:order_pk>/delete/', views.delete, name='delete', ),
    # This url will call the view that changes an existing order, and then send you to the Order page
    path('changeOrder/<int:order_pk>', views.changeOrder, name='changeOrder'),
    # URL for cooks to view current "cooking" orders
    path('cookOrder/', views.cookOrder, name='cookOrder'),
    # URL for cooks to view current ingredients
    path('ingredients/', views.ingredients, name='ingredients'),
    # URL for orders that are unable to be placed
    path('orderFailed/', views.order_failed, name='orderFailed'),
	# Button Changes the status of the order
	path('serverPage/button/', views.button, name='button')

]
