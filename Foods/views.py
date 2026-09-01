from django.shortcuts import render , redirect
from .models import FoodModel, CartModel , Order
from .forms import userRegistrationForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
import uuid
# Create your views here.

@login_required
def showitem(request):
    food = FoodModel.objects.all()

    for food_item in food:
        cart_item = CartModel.objects.filter(user = request.user , food = food_item).first()

        if cart_item:
            food_item.quantity = cart_item.quantity
        else:
            food_item.quantity = 0

    return render(request , 'home.html', {"food":food})

@login_required
def additem(request , food_id):
    if request.method == "POST":
        action = request.POST.get('action')
        food = get_object_or_404(FoodModel,id = food_id)
        cart_item , created = CartModel.objects.get_or_create(user = request.user , food = food, defaults={"quantity": 1})

        if action == 'increase':
            cart_item.quantity += 1

        elif action == 'decrease':
            cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete()

        else:
            cart_item.save()

    return redirect('showitem')

@login_required
def showcartitem(request):
    foodcart = CartModel.objects.filter(user = request.user)

    total_price = 0
    total_items = 0

    for item in foodcart:
        item.subtotal = item.quantity * item.food.price
        total_price += item.subtotal
        total_items += item.quantity

    return render(request , 'cartpage.html' , {"cart":foodcart,"total_price": total_price , "total_items" : total_items})

@login_required
def cartadditem(request, cart_id):
    if request.method == 'POST':
        action = request.POST.get('action')
        cart_item = get_object_or_404(CartModel, id = cart_id , user= request.user)

        if action == 'increase':
            cart_item.quantity += 1

        elif action == 'decrease':
            cart_item.quantity -= 1

        if cart_item.quantity <= 0:
            cart_item.delete()

        else:
            cart_item.save()

    return redirect('showcart')

def UserReg(request):
    if request.method == 'POST':
        form = userRegistrationForm(request.POST)
        if form.is_valid():  
            user = form.save()
            login(request,user)
            return redirect("showitem")
        
    else:
        form = userRegistrationForm()
    return render(request , 'register.html' , {"form": form})

def userLogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request , username = username , password = password)
        
        if user is not None and user.is_active:
            login(request,user)
            return redirect('showitem')
        
        else:
            return render(request , 'login.html',{'error' : 'invalid credential provided , please try again'})
        
    return render(request,'login.html')

@login_required
def userLogout(request):
    logout(request)
    return redirect('login')

@login_required
def checkout(request):

    cart_items = CartModel.objects.filter(
        user=request.user
    )

    total_price = 0

    for item in cart_items:
        total_price += item.food.price * item.quantity
        Order.objects.create(
            user=request.user,
            food=item.food,
            price=item.food.price,
            total_price = total_price,
            order_id=str(uuid.uuid4())
        )

    cart_items.delete()

    return render(request, 'success.html')