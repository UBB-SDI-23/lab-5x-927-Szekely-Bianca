from django.db import models

class Product(models.Model):
    product_name= models.CharField(max_length=50)
    product_price = models.FloatField()
    product_pieces= models.IntegerField()
    product_color = models.CharField(max_length=30)
    shopping_center = models.ManyToManyField('ShoppingCenter', through='ShoppingCenter_Product')

    def __str__(self):
        return f"{self.product_name} -- {self.product_price}"