from django.http.response import JsonResponse
from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth import authenticate , login ,logout
from django.shortcuts import redirect
from store.models import Product,Cart

from django.contrib.auth.decorators import login_required


def addtocart(request):
    if request.method == 'POST':
        if request.user.is_authenticated: #login
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id=prod_id)
            if(product_check):
                if(Cart.objects.filter(user=request.user.id, product_id=prod_id)):
                    return JsonResponse({'status': "Product Already in Cartd"})
                else:
                    prod_qty =  int(request.POST.get('product_qty'))
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user=request.user, product_id=prod_id,product_qty=prod_qty)
                        return JsonResponse({'status': "Product added successfully Cartd"})
                    else:
                        return JsonResponse({'status': "Only"+ str(product_check.quantity)+" quantity available"})
            else:
                return JsonResponse({'status': "No such product found"})
        else:
            return JsonResponse({'status': "Login to Continue"})
    return redirect('/')

@login_required(login_url='loginpage') # ไม่ให้เข้าถึงหากไม่ login

def viewcart(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, "store/template/store/cart.html", context)

def updatecart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(product_id=prod_id, user=request.user)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': "Update Successfully"})
    return redirect('/')

def deletecartitem(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if(Cart.objects.filter(user=request.user,product_id=prod_id)):
            cartitem = Cart.objects.get(product_id=prod_id,user=request.user)
            cartitem.delete()
        return JsonResponse({'status': "Remove Successfully"})
    return redirect('/')