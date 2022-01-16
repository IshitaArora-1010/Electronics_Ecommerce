from django.db import models
from .product import Product
from .customer import Customer
import datetime


class Order(models.Model):
    CHOICES = (("Agar Nagar",'Agar Nagar'),("Kitchlu Nagar",'Kitchlu Nagar'),("Rajguru Nagar",'Rajguru Nagar'),("Field Ganj",'Field Ganj'),("Khud Mohalla",'Khud Mohalla'),("Miller Ganj",'Miller Ganj'),("Sarabha Nagar",'Sarabha Nagar'),("BRS Nagar",'BRS Nagar'),("Brown Road",'Brown Road'),("Pakhowal Road",'Pakhowal Road'),("Ghumar Mandi",'Ghumar Mandi'),("Model Town",'Model Town'),("New Shivaji Nagar",'New Shivaji Nagar'),("New Hargobind Nagar",'New Hargobind Nagar'),("Shivaji Nagar",'Shivaji Nagar'),("Hargobind Nagar",'Hargobind Nagar'),("Industrial Area",'Industrial Area'),)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    # product_name = models.ForeignKey(Product.name, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # customer_name = models.ForeignKey(Customer.first_name, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    name = models.CharField(max_length=50, default='', blank=False)
    location = models.CharField(max_length=50, default='', blank=False, choices=CHOICES)
    address = models.CharField(max_length=50, default='', blank=False)
    email = models.CharField(max_length=50, default='', blank=False)
    phone = models.CharField(max_length=50, default='', blank=False)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id)


