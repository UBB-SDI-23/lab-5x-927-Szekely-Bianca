from django.db import models

class ShoppingCenter(models.Model):
    shop_code= models.IntegerField()
    shop_name= models.CharField(max_length=50)
    shop_category= models.CharField(max_length=50)
    nr_employee= models.IntegerField()
    shop_floor= models.IntegerField()
    products = models.ManyToManyField('Product', through='ShoppingCenter_Product')

    def __str__(self):
        return f"{self.shop_code} -- {self.shop_name}"