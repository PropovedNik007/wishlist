from django.contrib import admin

# Register your models here.
from .models import Product, WishList

admin.site.register(Product)
admin.site.register(WishList)
