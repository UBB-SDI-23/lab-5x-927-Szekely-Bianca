from django.urls import path

from .Views.EmployeeView import EmployeeDetail, EmployeeInfo, EmployeeWithSalaryAtLeastN
from .Views.ProductView import ProductDetail,ProductInfo
from .Views.ShoppingCenterView import ShoppingCenterDetail,ShoppingCenterInfo,\
    ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts,ShowTopFiveShopsWhichHaveMostDistinctProducts,ShoppingCenterCreateView
from .Views.ShoppingCenter_ProductView import ShoppingCenter_ProductDetail,ShoppingCenter_ProductInfo

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