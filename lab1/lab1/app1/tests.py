from django.test import TestCase
from lab1.lab1.app1.Models.ShoppingCenterModel import ShoppingCenter
from lab1.lab1.app1.Models.ProductModel import Product
from lab1.lab1.app1.Models.ShoppingCenter_ProductModel import ShoppingCenter_Product
from rest_framework.test import APIClient
from django.urls import reverse
# Create your tests here.

class ViewTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.shop1=ShoppingCenter.objects.create(
            shop_code= 5656,
            shop_name="SH1",
            shop_category= "cat1",
            nr_employee= 30,
            shop_floor=1)

        self.shop2=ShoppingCenter.objects.create(
            shop_code= 5555,
            shop_name="SH2",
            shop_category= "cat2",
            nr_employee= 50,
            shop_floor=2)

        self.shop3=ShoppingCenter.objects.create(
            shop_code= 1111,
            shop_name="SH3",
            shop_category= "cat3",
            nr_employee= 10,
            shop_floor=0)

        self.shop4=ShoppingCenter.objects.create(
            shop_code= 2222,
            shop_name="SH4",
            shop_category= "cat4",
            nr_employee= 20,
            shop_floor=2)

        self.shop5=ShoppingCenter.objects.create(
            shop_code= 3333,
            shop_name="SH5",
            shop_category= "cat5",
            nr_employee= 40,
            shop_floor=1)


        self.product1 = Product.objects.create(
            product_name= "PROD1",
            product_price = 56.45,
            product_pieces= 400,
            product_color = "col1")

        self.product2 = Product.objects.create(
            product_name= "PROD2",
            product_price = 70.30,
            product_pieces= 800,
            product_color = "col2")

        self.product3 = Product.objects.create(
            product_name= "PROD3",
            product_price = 10.10,
            product_pieces= 100,
            product_color = "col3")

        self.product4 = Product.objects.create(
            product_name= "PROD4",
            product_price = 23.34,
            product_pieces= 200,
            product_color = "col4")

        self.product5 = Product.objects.create(
            product_name= "PROD5",
            product_price= 44.70,
            product_pieces=300,
            product_color= "col5")

        self.prod_shop1=ShoppingCenter_Product.objects.create(
            quantity= 10,
            availability= "YES",
            discount= 10.0,
            shop= self.shop1,
            product= self.product1)

        self.prod_shop2=ShoppingCenter_Product.objects.create(
            quantity= 20,
            availability= "YES",
            discount= 20.0,
            shop= self.shop2,
            product= self.product2)

        self.prod_shop3=ShoppingCenter_Product.objects.create(
            quantity= 30,
            availability= "YES",
            discount= 30.0,
            shop= self.shop3,
            product= self.product3)

        self.prod_shop4=ShoppingCenter_Product.objects.create(
            quantity= 40,
            availability= "YES",
            discount= 15.0,
            shop= self.shop3,
            product= self.product1)

        self.prod_shop5=ShoppingCenter_Product.objects.create(
            quantity= 50,
            availability= "YES",
            discount= 20.0,
            shop= self.shop4,
            product= self.product4)

        self.prod_shop6=ShoppingCenter_Product.objects.create(
            quantity= 60,
            availability= "YES",
            discount= 20.0,
            shop= self.shop5,
            product= self.product5)

        self.prod_shop7=ShoppingCenter_Product.objects.create(
            quantity= 70,
            availability= "YES",
            discount= 20.0,
            shop= self.shop5,
            product= self.product1)

        self.prod_shop8=ShoppingCenter_Product.objects.create(
            quantity= 80,
            availability= "YES",
            discount= 20.0,
            shop= self.shop5,
            product= self.product4)

        self.shop1.products.add(self.product1) #56.45
        self.shop2.products.add(self.product2) #70.30


        self.shop3.products.add(self.product3) #33.275
        self.shop3.products.add(self.product1)

        self.shop4.products.add(self.product4) #23.34

        self.shop5.products.add(self.product5) #41.496666666666667
        self.shop5.products.add(self.product1)
        self.shop5.products.add(self.product4)

        2,1,5,3,4


    def test_ShowAllTheShopsOrderedByTheAveragePriceOfTheirProducts(self):
        url=reverse('avg_price')
        response=self.client.get(url)
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.json(), [ {"id": self.shop4.id, "shop_code" : 2222, "shop_name" : "SH4", "shop_category" : "cat4",
                                            "nr_employee" : 20, "shop_floor" : 2, "avg_price" : 23.34, "products":[4]},
                                            {"id": self.shop3.id, "shop_code": 1111, "shop_name": "SH3",
                                             "shop_category": "cat3",
                                             "nr_employee": 10, "shop_floor": 0, "avg_price": 33.275,
                                             "products": [3,1]},
                                            {"id": self.shop5.id, "shop_code": 3333, "shop_name": "SH5",
                                             "shop_category": "cat5",
                                             "nr_employee": 40, "shop_floor": 1, "avg_price": 41.496666666666667, "products": [5,1,4]},
                                            {"id": self.shop1.id, "shop_code": 5656, "shop_name": "SH1",
                                             "shop_category": "cat1",
                                             "nr_employee": 30, "shop_floor": 1, "avg_price": 56.45,
                                             "products": [1]},
                                            {"id": self.shop2.id,"shop_code": 5555, "shop_name":"SH2", "shop_category": "cat2", "nr_employee":50,
                                            "shop_floor":2,"avg_price":70.30,"products":[2]}
                                            ])

    def test_ShowTopFiveShopsWhichHaveMostDistinctProducts(self):
        url = reverse('count_prod')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 5)
        self.assertEqual(response.json(),[ {"id": self.shop5.id, "shop_code" : 3333, "shop_name" : "SH5", "shop_category" : "cat5",
                                            "nr_employee" : 40, "shop_floor" : 1,"count_product": 3, "products":[5,1,4]},
                                           {"id": self.shop3.id, "shop_code": 1111, "shop_name": "SH3","shop_category": "cat3",
                                            "nr_employee": 10, "shop_floor": 0,"count_product": 2,"products": [3,1]},
                                           {"id": self.shop1.id, "shop_code": 5656, "shop_name": "SH1","shop_category": "cat1",
                                            "nr_employee": 30, "shop_floor": 1,"count_product": 1,"products": [1]},
                                           {"id": self.shop2.id, "shop_code": 5555, "shop_name": "SH2","shop_category": "cat2", "nr_employee": 50,
                                            "shop_floor": 2,"count_product": 1, "products": [2]},
                                           {"id": self.shop4.id, "shop_code": 2222, "shop_name": "SH4","shop_category": "cat4",
                                            "nr_employee": 20, "shop_floor": 2,"count_product": 1, "products": [4]}
                                           ])
