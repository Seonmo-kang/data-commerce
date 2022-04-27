# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Category(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'category'


class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    # TODO user에 따라 바뀌어야 함.
    seller = models.ForeignKey("user", related_name="seller", on_delete=models.CASCADE, db_column="id")
    category = models.ForeignKey("category", related_name="product_category", on_delete=models.SET_NULL, db_column="id")
    file = models.FileField()
    title = models.CharField(max_length=30, blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    price = models.BigIntegerField()
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'product'


class Views(models.Model):
    product = models.ForeignKey("product", related_name="product_view", on_delete=models.CASCADE, db_column="id")
    price = models.IntegerField()
    create_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'views'


class Wish(models.Model):
    id = models.BigAutoField(primary_key=True)
    # TODO user에 따라 바뀌어야 함.
    user = models.ForeignKey("user", related_name="user_wish", on_delete=models.CASCADE, db_column="id")
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'wish'


class Cart(models.Model):
    id = models.BigAutoField(primary_key=True)
    # TODO user에 따라 바뀌어야 함.
    user = models.ForeignKey("user", related_name="user_cart", on_delete=models.CASCADE, db_column="id")
    create_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        managed = False
        db_table = 'cart'
