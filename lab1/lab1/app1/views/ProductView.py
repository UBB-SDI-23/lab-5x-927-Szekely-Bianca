from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from lab1.lab1.app1.models.EmployeeModel import Employee
from lab1.lab1.app1.models.ProductModel import Product
from lab1.lab1.app1.models.ShoppingCenterModel import ShoppingCenter
from lab1.lab1.app1.models.ShoppingCenter_ProductModel import ShoppingCenter_Product
from lab1.lab1.app1.serializer.EmployeeSerializer import EmployeeSerializer, EmployeeIdSerializer
from lab1.lab1.app1.serializer.ProductSerializer import ProductSerializer
from lab1.lab1.app1.serializer.ShoppingCenterSerializer import ShoppingCenterSerializer, ShoppingCenterIdSerializer
from lab1.lab1.app1.serializer.ShoppingCenter_ProductSerializer import ShoppingCenter_ProductSerializer

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
