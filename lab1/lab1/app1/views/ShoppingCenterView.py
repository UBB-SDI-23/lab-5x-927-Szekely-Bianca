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


class ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts(generics.ListAPIView):
    serializer_class = ShoppingCenterSerializer
    def get_queryset(self):
        query = ShoppingCenter.objects \
            .annotate(avg_price=Avg('products__product_price')) \
            .order_by('avg_price')
        print(query.query)
        return query