from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=150)
    rent = models.FloatField()
    category = models.ManyToManyField(Category, related_name="product")

    def __str__(self):
        return self.name


class BookProduct(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    rent_from = models.DateField()
    rent_to = models.DateField()
    