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

    # ex: /init/
    # This url is for testing/developing purposes ONLY
    # TODO: delete this in production version
    path('init/', views.init, name='init')
]
