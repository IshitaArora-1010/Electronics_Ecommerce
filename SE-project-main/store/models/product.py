from django.db import models
from .category import Category


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    saleprice = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField(default='')
    brand = models.TextField(default='', blank=True)
    dimensions = models.CharField(max_length=50, default='', blank=True)
    image = models.ImageField(upload_to='uploads/products/')
    objects = models.Manager()

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in=ids)

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category=category_id)
        else:
            return Product.get_all_products()

    @staticmethod
    def get_all_products_by_category_name(category_name):
        if category_name:
            return Product.objects.filter(category=category_name)
        else:
            return Product.get_all_products()  

    @staticmethod
    def get_all_products_by_product_name(name):
        if name:
            print(name)
            return Product.objects.filter(name__icontains=name).order_by('-id')
        else:
            return Product.get_all_products()  


