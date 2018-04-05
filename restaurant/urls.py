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
    path('customerOrder/<int:order_pk>/delete/', views.delete, name='delete')
]
