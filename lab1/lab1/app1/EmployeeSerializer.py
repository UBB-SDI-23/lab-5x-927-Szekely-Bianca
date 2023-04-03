from rest_framework import serializers
from .EmployeeModel import Employee
from .ShoppingCenterModel import ShoppingCenter


class EmployeeSerializer(serializers.ModelSerializer):
    employee_firstname = serializers.CharField(max_length=50)
    employee_lastname = serializers.CharField(max_length=50)
    employee_salary = serializers.FloatField()
    employee_age = serializers.IntegerField()
    employee_phone = serializers.IntegerField()

    employee_shop = ShoppingCenter()

    def validate_shop_id(self,val):
        filter= ShoppingCenter.objects.filter(id=val)
        if not filter.exists():
            raise serializers.ValidationError("Shop does not exist!")
        return val

    class Meta:
        model = Employee
        fields = "__all__"



class EmployeeIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        #fields = "__all__"
        fields = ("id",)

    # def create(self, validated_data):
    #     employee_shop = self.context.get('employee_shop', None) # get the id of the shopping center instance from context
    #     if employee_shop is not None:
    #         validated_data['employee_shop_id'] = employee_shop # set the employee_shop_id field to the id of the shopping center instance
    #     return super().create(validated_data)
