from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Product(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
