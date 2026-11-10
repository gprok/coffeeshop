from django.contrib import admin

from .models import Beverage, Customer, Order, OrderDetail

admin.site.register(Beverage)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderDetail)
