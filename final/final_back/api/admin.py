from django.contrib import admin
from api.models import Product, UserProduct


@admin.register(UserProduct)
class UserProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'count')

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity')