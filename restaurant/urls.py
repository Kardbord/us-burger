from django.urls import path

from . import views

app_name = 'restaurant'
urlpatterns = [
    # ex: /restaurant/
    path('', views.index, name='index'),
    # ex: /restaurant/customerMenu/
    path('customerMenu/', views.customerMenu, name='customerMenu'),
    # ex: /restaurant/customerOrder/
    path('customerOrder/', views.customerOrder, name='customerOrder'),
]