from rest_framework import serializers
from lab1.lab1.app1.models.EmployeeModel import Employee
from lab1.lab1.app1.models.ShoppingCenterModel import ShoppingCenter
from lab1.lab1.app1.models.ProductModel import Product
from lab1.lab1.app1.models.ShoppingCenter_ProductModel import ShoppingCenter_Product

class ProductSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(max_length=50)
    product_price = serializers.FloatField()
    product_pieces = serializers.IntegerField()
    product_color = serializers.CharField(max_length=30)

    #num_shops = serializers.SerializerMethodField()

    #shopping_center = ShoppingCenter_ProductSerializer(many=True)

    class Meta:
        model = Product
        fields = "__all__"

    # def get_num_shops(self, obj):
    #     return len(obj.shopping_center.all())


