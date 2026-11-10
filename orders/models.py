from django.db import models
from django.contrib.auth.models import User


class Beverage(models.Model):
    class Category(models.TextChoices):
        COFFEE = "coffee", "Coffee"
        JUICE = "juice", "Juice"
        TEA = "tea", "Tea"
        WATER = "water", "Water"

    name = models.CharField(max_length=40)
    category = models.CharField(max_length=20, choices=Category.choices)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name



class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "pending", "Pending"
        CANCELLED = "cancelled", "Cancelled"
        SHIPPED = "shipped", "Shipped"
        DELIVERED = "delivered", "Delivered"

    customer = models.ForeignKey(Customer, on_delete=models.RESTRICT)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="orders_created")
    deliverd_by = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="orders_delivered")

    def __str__(self):
        return self.customer.name + " " + str(self.order_date)


class OrderDetail(models.Model):
    order = models.ForeignKey(Order, on_delete=models.RESTRICT)
    beverage = models.ForeignKey(Beverage, on_delete=models.RESTRICT)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.order.__str__() + " " + self.beverage.name
