from django.urls import path
from . import views

from store.template.store.controller import authview,cart,checkout,order

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('', views.home, name="index"),
    path('home/', views.home,name="home"),
    path('collections', views.collections,name="collections"),
    path('collections/<str:slug>',views.collectionsview, name="collectionsview"),
    path('collections/<str:cate_slug>/<str:prod_slug>', views.productview, name="productview"),

    path('register/',authview.register, name="register"),

    path('login/',authview.loginpage, name="loginpage"),

    path('logout/', authview.logoutpage, name="logoutpage"),

    path('add-to-cart', cart.addtocart,name="addtocart"),

    path('cart',cart.viewcart,name="cart"),

    path('update-cart',cart.updatecart,name="updatecart"),

    path('delete-cart-item',cart.deletecartitem,name="deletecartitem"),

    path('checkout',checkout.index, name="checkout"),

    path('place-order',checkout.placeorder, name="placeorder"),

    path('my-history',order.index, name="myorders"),

    path('view-order/<str:r_no>/', order.vieworders, name="orderview"),
]
