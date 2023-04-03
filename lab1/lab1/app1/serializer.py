# from rest_framework import serializers
# from .models import Employee, Product, ShoppingCenter,ShoppingCenter_Product
#
#
# class EmployeeSerializer(serializers.ModelSerializer):
#     employee_firstname = serializers.CharField(max_length=50)
#     employee_lastname = serializers.CharField(max_length=50)
#     employee_salary = serializers.FloatField()
#     employee_age = serializers.IntegerField()
#     employee_phone = serializers.IntegerField()
#
#     employee_shop = ShoppingCenter()
#
#     def validate_shop_id(self,val):
#         filter= ShoppingCenter.objects.filter(id=val)
#         if not filter.exists():
#             raise serializers.ValidationError("Shop does not exist!")
#         return val
#
#     class Meta:
#         model = Employee
#         fields = "__all__"
#
#
#
# class EmployeeIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Employee
#         #fields = "__all__"
#         fields = ("id",)
#
#     # def create(self, validated_data):
#     #     employee_shop = self.context.get('employee_shop', None) # get the id of the shopping center instance from context
#     #     if employee_shop is not None:
#     #         validated_data['employee_shop_id'] = employee_shop # set the employee_shop_id field to the id of the shopping center instance
#     #     return super().create(validated_data)
#
#
# class ShoppingCenterIdSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = ShoppingCenter
#         #fields = "__all__"
#         fields=("id",)
#
#
# class ShoppingCenter_ProductSerializer(serializers.ModelSerializer):
#     shop = ShoppingCenter()
#     product = Product()
#     quantity = serializers.IntegerField()
#     availability = serializers.CharField(max_length=10)
#     discount = serializers.FloatField()
#
#
#     def validate_shopp_id(self,val):
#         filter= ShoppingCenter.objects.filter(id=val)
#         if not filter.exists():
#             raise serializers.ValidationError("Shop does not exist!")
#         return val
#
#     def validate_product_id(self,val):
#         filter= Product.objects.filter(id=val)
#         if not filter.exists():
#             raise serializers.ValidationError("Product does not exist!")
#         return val
#
#     class Meta:
#         model = ShoppingCenter_Product
#         fields = "__all__"
#
# class ShoppingCenterSerializer(serializers.ModelSerializer):
#     shop_code= serializers.IntegerField()
#     shop_name= serializers.CharField(max_length=50)
#     shop_category= serializers.CharField(max_length=50)
#     nr_employee= serializers.IntegerField()
#     shop_floor= serializers.IntegerField()
#
#     employees=EmployeeSerializer(many=True,read_only=True)
#
#
#     avg_price=serializers.FloatField(read_only=True)
#     count_product=serializers.IntegerField(read_only=True)
#     #num_product=serializers.SerializerMethodField()
#
#     #products = ShoppingCenter_ProductSerializer(many=True)
#     class Meta:
#         model = ShoppingCenter
#         fields = "__all__"
#
#     # def get_num_product(self, obj):
#     #     return len(obj.products.all())
#
#
# class ProductSerializer(serializers.ModelSerializer):
#     product_name = serializers.CharField(max_length=50)
#     product_price = serializers.FloatField()
#     product_pieces = serializers.IntegerField()
#     product_color = serializers.CharField(max_length=30)
#
#     #num_shops = serializers.SerializerMethodField()
#
#     #shopping_center = ShoppingCenter_ProductSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = "__all__"
#
#     # def get_num_shops(self, obj):
#     #     return len(obj.shopping_center.all())
#
#
