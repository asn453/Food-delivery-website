from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.showitem, name = 'showitem'),
    path('add/<int:food_id>/',views.additem, name = 'additem'),
    path('cart/',views.showcartitem , name ='showcart'),
    path('cartupdate/<int:cart_id>/',views.cartadditem , name='cartupdate'),
    path('register/',views.UserReg, name='UserReg'),
    path('login/',views.userLogin , name = 'login'),
    path('logout/' , views.userLogout , name ='logout'),
    path('checkout/', views.checkout, name='checkout'),
]