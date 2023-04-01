from django.urls import path,include
from rest_framework_swagger.views import get_swagger_view

from .views import EmployeeDetail, EmployeeInfo, EmployeeWithSalaryAtLeastN
from .views import ProductDetail,ProductInfo
from .views import ShoppingCenterDetail,ShoppingCenterInfo
from .views import ShoppingCenter_ProductDetail,ShoppingCenter_ProductInfo
from .views import ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts,ShowTopFiveShopsWhichHaveMostDistinctProducts
from .views import ShoppingCenterCreateView
from rest_framework.documentation import include_docs_urls
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from django.contrib import admin



urlpatterns=[
    path("ShoppingCenter/",ShoppingCenterDetail.as_view(),name="ShoppingCenter"),
    path("ShoppingCenter/<int:id>/",ShoppingCenterInfo.as_view()),
    path("Employee/",EmployeeDetail.as_view(),name="Employee"),
    path("Employee/<int:id>/",EmployeeInfo.as_view()),
    path("Product/",ProductDetail.as_view(),name="Product"),
    path("Product/<int:id>/",ProductInfo.as_view()),
    path("Salary/<int:sal>/",EmployeeWithSalaryAtLeastN.as_view(),name="sal"),
    path("ShoppingCenter_Product/",ShoppingCenter_ProductDetail.as_view(),name="ShoppingCenter_Product"),
    path("ShoppingCenter_Product/<int:id>/",ShoppingCenter_ProductInfo.as_view()),
    path("ShoppingCenter/AveragePrice/",ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts.as_view(),name='avg_price'),
    path("ShoppingCenter/CountProducts/",ShowTopFiveShopsWhichHaveMostDistinctProducts.as_view(),name='count_prod'),
    path("ShoppingCenter/<int:id>/Employee/", ShoppingCenterCreateView.as_view())
]