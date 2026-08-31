from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FoodModel(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    description = models.TextField()
    image = models.ImageField(upload_to='food1')

    def __str__(self):
        return self.name

class CartModel(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    food = models.ForeignKey(FoodModel,on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.user
    
class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    order_id = models.CharField(max_length=100)
    food = models.ForeignKey(FoodModel, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8 , decimal_places=2)
    total_price = models.DecimalField(max_digits=10 , decimal_places=2)

    def __str__(self):
        return self.order_id