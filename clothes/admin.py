from django.contrib import admin

from .models import Product, BookProduct, Category
# Register your models here.


admin.site.register(Product)
admin.site.register(BookProduct)
admin.site.register(Category)