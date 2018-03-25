from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    # ex: /restaurant/
    path('', views.index, name='index'),
    # ex: /restaurant/customerMenu/
    path('customerMenu/', views.customerMenu, name='customerMenu'),

    # ex: /restaurant/customerOrder/1
    # path('customerOrder/<int:order_pk>/', views.customerOrder, name='customerOrder'),
    # TODO: delete the line below and uncomment the line above once customerMenu sends an order_pk as an arg to customerOrder
    # ex: /restaurant/customerOrder/
    path('customerOrder/', views.customerOrder, name='customerOrder')
]
