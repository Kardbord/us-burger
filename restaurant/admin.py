from django.contrib import admin

# from .models import MenuItem, SupplyItem, Order, OrderItem, Menu
from .models import *


class OrderItemInline(admin.StackedInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['pin']}),
        ('Order Validity', {'fields': ['order_items_are_available']}),
    ]

    inlines = [OrderItemInline]


# Register your models here.
admin.site.register(MenuItem)
admin.site.register(SupplyItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Menu)
admin.site.register(SupplyAmt)
