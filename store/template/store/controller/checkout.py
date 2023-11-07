from django.http.response import JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
import random
from django.shortcuts import render
from django.contrib.auth import authenticate , login ,logout
from django.shortcuts import redirect
from store.models import Product,Cart,Order,Profile,OrderItem

from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

@login_required(login_url='loginpage') # ไม่ให้เข้าถึงหากไม่ login
def index(request):
    rawcart = Cart.objects.filter(user=request.user)
    for item in rawcart:
        if item.product_qty > item.product.quantity:
            Cart.objects.delete(id=item.id)
    cartitems = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cartitems:
        total_price = total_price + item.product.selling_price * item.product_qty
        
    userprofile = Profile.objects.filter(user=request.user.id).first()

    context = {'cartitems':cartitems, 'total_price':total_price,'userprofile':userprofile}
    return render(request,"store/template/store/checkout.html",context)

@login_required(login_url='loginpage') # ไม่ให้เข้าถึงหากไม่ login
def placeorder(request):
    if request.method == 'POST':

        currentuser = User.objects.filter(id=request.user.id).first()

        if not currentuser.first_name : 
            currentuser.first_name = request.POST.get('fname')
            currentuser.last_name = request.POST.get('lanme')
            currentuser.save()

        if not Profile.objects.filter(user=request.user):
            userprofile = Profile()
            userprofile.user = request.user
            userprofile.fname = request.POST.get('fname')
            userprofile.lname = request.POST.get('lname')
            userprofile.email = request.POST.get('email')
            userprofile.phone = request.POST.get('phone')
            userprofile.save()


        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')

        neworder.payment_mode = request.POST.get('payment_mode')

        cart = Cart.objects.filter(user=request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price = cart_total_price + item.product.selling_price * item.product_qty

        neworder.total_price = cart_total_price        
        redeemno = str(random.randint(1111111111,9999999999))
        while Order.objects.filter(redeem_code=redeemno) is None:
            redeemno = str(random.randint(1111111111,9999999999))
        
        neworder.redeem_code = redeemno
        neworder.save()

        neworderitems = Cart.objects.filter(user=request.user)
        for item in neworderitems:
            orderproduct = Product.objects.filter(id=item.product_id).first()
            orderproduct.quantity = orderproduct.quantity - item.product_qty
            
        
        
        Cart.objects.filter(user=request.user).delete()

        messages.success(request,"Your order Payment Sucessfully")

    return redirect('/')

