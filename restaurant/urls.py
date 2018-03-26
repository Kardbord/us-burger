from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    # ex: /restaurant/
    path('', views.index, name='index'),
    # ex: /restaurant/customerMenu/
    path('customerMenu/', views.customerMenu, name='customerMenu'),
    # the path that customerMenu.html's form's action is set to.
    path('newOrder', views.newOrder, name='newOrder'),
    # ex: /restaurant/customerOrder/1
    # TODO: Modify this url path if needed according to when it is called by reverse() in views.py
    path('customerOrder/<int:order_pk>/', views.customerOrder, name='customerOrder'),
]
