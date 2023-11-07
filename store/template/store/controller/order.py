from django.http.response import JsonResponse
from django.contrib import messages

from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import login_required
import random
from django.shortcuts import render
from django.contrib.auth import authenticate , login ,logout
from django.shortcuts import redirect
from store.models import Product,Cart,Order,Profile,OrderItem

from store import urls

from django.shortcuts import get_object_or_404


from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required

def index(request):
    orders = Order.objects.filter(user=request.user)
    context = {'orders':orders}

    return render(request,"store/template/store/orders/index.html",context)


def vieworders(request , r_no):
    order = Order.objects.filter(redeem_code=r_no).filter(user=request.user).first()
    ordersview = OrderItem.objects.filter(order=order)
    context = {'order': order, 'ordersview': ordersview}
    return render(request, "store\template\store\orders\view.html",context)