from django.contrib import admin

from .models import MenuItem, SupplyItem, Order, OrderItem

# Register your models here.
admin.site.register(MenuItem)
admin.site.register(SupplyItem)
admin.site.register(Order)
admin.site.register(OrderItem)
