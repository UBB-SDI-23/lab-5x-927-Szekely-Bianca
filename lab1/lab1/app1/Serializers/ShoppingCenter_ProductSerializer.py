from rest_framework import serializers
from ..Models.ShoppingCenterModel import ShoppingCenter
from ..Models.ProductModel import Product
from ..Models.ShoppingCenter_ProductModel import ShoppingCenter_Product


class ShoppingCenter_ProductSerializer(serializers.ModelSerializer):
    shop = ShoppingCenter()
    product = Product()
    quantity = serializers.IntegerField()
    availability = serializers.CharField(max_length=10)
    discount = serializers.FloatField()

    def validate_shopp_id(self, val):
        filter = ShoppingCenter.objects.filter(id=val)
        if not filter.exists():
            raise serializers.ValidationError("Shop does not exist!")
        return val

    def validate_product_id(self, val):
        filter = Product.objects.filter(id=val)
        if not filter.exists():
            raise serializers.ValidationError("Product does not exist!")
        return val

    class Meta:
        model = ShoppingCenter_Product
        fields = "__all__"
