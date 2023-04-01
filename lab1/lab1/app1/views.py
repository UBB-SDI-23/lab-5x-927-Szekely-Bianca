from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .models import Employee
from .models import Product
from .models import ShoppingCenter
from .models import ShoppingCenter_Product
from .serializer import EmployeeSerializer, EmployeeIdSerializer
from .serializer import ProductSerializer
from .serializer import ShoppingCenterSerializer, ShoppingCenterIdSerializer
from .serializer import ShoppingCenter_ProductSerializer


# Create your views here.

class EmployeeDetail(APIView):
    def get(self, request):
        obj = Employee.objects.all()
        # serializer = EmployeeIdSerializer(obj,many=True)
        serializer = EmployeeSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class EmployeeInfo(APIView):
    def get(self, request, id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = EmployeeSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = EmployeeSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Employee.objects.get(id=id)
        except Employee.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class ProductDetail(APIView):
    def get(self, request):
        obj = Product.objects.all()
        serializer = ProductSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ProductInfo(APIView):
    def get(self, request, id):
        try:
            obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ProductSerializer(obj)
        # serializer=ShoppingCenter_ProductSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(obj, data=request.data)
        # serializer = ShoppingCenter_ProductSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ProductSerializer(obj, data=request.data, partial=True)
        # serializer = ShoppingCenter_ProductSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = Product.objects.get(id=id)
        except Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class ShoppingCenterDetail(APIView):
    def get(self, request):
        obj = ShoppingCenter.objects.all()
        # serializer = ShoppingCenterIdSerializer(obj,many=True)
        serializer = ShoppingCenterSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShoppingCenterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    # serializer_class = ShoppingCenterSerializer


class ShoppingCenterInfo(APIView):
    def get(self, request, id):
        try:
            obj = ShoppingCenter.objects.get(id=id)
        except ShoppingCenter.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingCenterSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = ShoppingCenter.objects.get(id=id)
        except ShoppingCenter.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoppingCenterSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = ShoppingCenter.objects.get(id=id)
        except ShoppingCenter.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoppingCenterSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = ShoppingCenter.objects.get(id=id)
        except ShoppingCenter.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class EmployeeWithSalaryAtLeastN(APIView):
    def get(self, request, sal):
        salary = Employee.objects.filter(employee_salary__gte=sal)
        serializer = EmployeeSerializer(salary, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ShoppingCenter_ProductDetail(APIView):
    def get(self, request):
        obj = ShoppingCenter_Product.objects.all()
        serializer = ShoppingCenter_ProductSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ShoppingCenter_ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class ShoppingCenter_ProductInfo(APIView):
    def get(self, request, id):
        try:
            obj = ShoppingCenter_Product.objects.get(id=id)
        except ShoppingCenter_Product.DoesNotExist:
            msg = {"msg": "not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        serializer = ShoppingCenter_ProductSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id):
        try:
            obj = ShoppingCenter_Product.objects.get(id=id)
        except ShoppingCenter_Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoppingCenter_ProductSerializer(obj, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = ShoppingCenter_Product.objects.get(id=id)
        except ShoppingCenter_Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serializer = ShoppingCenter_ProductSerializer(obj, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            obj = ShoppingCenter_Product.objects.get(id=id)
        except ShoppingCenter_Product.DoesNotExist:
            msg = {"msg": "not found error"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

        obj.delete()
        return Response({"msg": "deleted"}, status=status.HTTP_204_NO_CONTENT)


class ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts(generics.ListAPIView):
    serializer_class = ShoppingCenterSerializer

    def get_queryset(self):
        query = ShoppingCenter.objects \
            .annotate(avg_price=Avg('products__product_price')) \
            .order_by('avg_price')
        print(query.query)

        return query


class ShowTopFiveShopsWhichHaveMostDistinctProducts(generics.ListAPIView):
    serializer_class = ShoppingCenterSerializer

    def get_queryset(self):
        query = ShoppingCenter.objects \
                    .annotate(count_product=Count('products__product_pieces')) \
                    .order_by('-count_product')[:5]
        print(query.query)

        return query


class ShoppingCenterCreateView(APIView):
    def post(self, request, id):
        shopping_center_data = request.data
        msg = "CREATED"

        for sh in shopping_center_data:
            sh['employee_shop'] = id
            print(sh)
            serializer = EmployeeSerializer(data=sh)
            if serializer.is_valid():
                serializer.save()
        return Response(msg, status=status.HTTP_201_CREATED)
