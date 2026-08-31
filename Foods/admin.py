from django.contrib import admin
from .models import FoodModel , CartModel

# Register your models here.
class Foodadmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'description' , 'image']
    search_fields = ['name']

class CartAdmin(admin.ModelAdmin):
    list_display = ['user' , 'food' , 'quantity']

admin.site.register(FoodModel,Foodadmin)
admin.site.register(CartModel,CartAdmin)