from rest_framework import serializers
from ..Models.ShoppingCenterModel import ShoppingCenter
from .EmployeeSerializer import EmployeeSerializer
from .ShoppingCenter_ProductSerializer import ShoppingCenter_ProductSerializer
from .ProductSerializer import ProductSerializer

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

    products = ProductSerializer(many=True,read_only=True)
    class Meta:
        model = ShoppingCenter
        fields = "__all__"

    # def get_num_product(self, obj):
    #     return len(obj.products.all())
