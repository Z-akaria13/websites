from django.contrib import admin

# Register your models here.
from .models import Order, Product

admin.site.register(Order)
admin.site.register(Product)