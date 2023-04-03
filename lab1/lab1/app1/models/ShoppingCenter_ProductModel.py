from django.db import models
from app1.models.ProductModel import Product
from app1.models.ShoppingCenterModel import ShoppingCenter

class ShoppingCenter_Product(models.Model):
    shop = models.ForeignKey(ShoppingCenter, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    availability = models.CharField(max_length=10)
    discount=models.FloatField()

    def __str__(self):
        return f"{self.shop}, {self.product} -- {self.quantity} - {self.availability}"
