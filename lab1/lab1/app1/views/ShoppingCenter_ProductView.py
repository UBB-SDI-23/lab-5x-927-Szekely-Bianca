from django.db.models import Avg, Count, OuterRef, Subquery, Q, Case, When, \
    IntegerField, Exists
from rest_framework import generics
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from app1.models.ShoppingCenter_ProductModel import ShoppingCenter_Product
from app1.serializer.ShoppingCenter_ProductSerializer import ShoppingCenter_ProductSerializer

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
