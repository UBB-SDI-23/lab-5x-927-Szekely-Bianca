from rest_framework import serializers
from lab1.lab1.app1.models.EmployeeModel import Employee
from lab1.lab1.app1.models.ShoppingCenterModel import ShoppingCenter
from lab1.lab1.app1.models.ProductModel import Product
from lab1.lab1.app1.models.ShoppingCenter_ProductModel import ShoppingCenter_Product
from lab1.lab1.app1.serializer.EmployeeSerializer import EmployeeSerializer

class ShoppingCenterIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCenter
        #fields = "__all__"
        fields=("id",)

class ShoppingCenterSerializer(serializers.ModelSerializer):
    shop_code= serializers.IntegerField()
    shop_name= serializers.CharField(max_length=50)
    shop_category= serializers.CharField(max_length=50)
    nr_employee= serializers.IntegerField()
    shop_floor= serializers.IntegerField()

    employees=EmployeeSerializer(many=True,read_only=True)


    avg_price=serializers.FloatField(read_only=True)
    count_product=serializers.IntegerField(read_only=True)
    #num_product=serializers.SerializerMethodField()

    #products = ShoppingCenter_ProductSerializer(many=True)
    class Meta:
        model = ShoppingCenter
        fields = "__all__"

    # def get_num_product(self, obj):
    #     return len(obj.products.all())
