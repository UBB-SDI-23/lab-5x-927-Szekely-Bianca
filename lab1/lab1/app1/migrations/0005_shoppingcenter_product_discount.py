# Generated by Django 4.1.7 on 2023-03-18 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_product_shopping_center_shoppingcenter_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='shoppingcenter_product',
            name='discount',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
