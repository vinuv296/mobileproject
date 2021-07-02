from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm, PlaceOrderForm
from django.contrib.auth import authenticate, login, logout
from owner.models import Product, Cart, Orders
from owner.views import get_object as get_product
from .decorators import loginrequired, permissionrequired
from django.db.models import Sum


# Create your views here.


#  auth

# registration
# login
# logout
# viewproduct
# add to cart
# place order
# manage order

def index(request):
    return render(request, "index.html")


def get_cart_count(user):
    cart_count = Cart.objects.filter(user=user, status="ordernotplaced").count()
    return cart_count


def registration(request, *args, **kwargs):
    form = UserRegistrationForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "login.html")
        else:
            context["form"] = form
    return render(request, "registration.html", context)


def login_view(request, *args, **kwargs):
    form = LoginForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect("user_home")
    return render(request, "login.html", context)


def log_out(request, *args, **kwargs):
    logout(request)
    return redirect("signin")


@loginrequired
def user_home(request, *args, **kwargs):
    mobiles = Product.objects.all()
    cart_count = get_cart_count(request.user)
    context = {
        "mobiles": mobiles,
        "cart_count": cart_count
    }
    return render(request, "home.html", context)


@loginrequired
def item_details(request, *args, **kwargs):
    id = kwargs.get('id')
    mobile = Product.objects.get(id=id)
    cart_count = get_cart_count(request.user)
    context = {
        "mobile": mobile,
        "cart_count": cart_count
    }
    return render(request, "item_detail.html", context)


@loginrequired
def add_to_cart(request, *args, **kwargs):
    pid = kwargs.get('id')
    product = get_product(pid)
    cart = Cart(product=product, user=request.user)
    cart.save()
    return redirect("carts")


@loginrequired
def my_cart(request, *args, **kwargs):
    cart_items = Cart.objects.filter(user=request.user, status="ordernotplaced")
    total = Cart.objects.filter(user=request.user, status="ordernotplaced").aggregate(Sum('product__price'))
    cart_count = get_cart_count(request.user)
    context = {
        "cart_items": cart_items,
        "total": total.get("product__price__sum"),
        "cart_count": cart_count
    }
    return render(request, "mycart.html", context)


@loginrequired
@permissionrequired
def delete_product_cart(request, *args, **kwargs):
    cid = kwargs.get("id")
    cart = Cart.objects.get(id=cid)
    cart.delete()
    return redirect("carts")


def place_order(request, *args, **kwargs):
    pid = kwargs.get("id")
    mobile = get_product(pid)
    cart_count = get_cart_count(request.user)
    context = {
        "form": PlaceOrderForm(initial={"product": mobile.mobile_name}),
        "cart_count": cart_count
    }
    print(kwargs)
    if request.method == "POST":
        print(kwargs)
        cid = kwargs.get("cid")
        cart = Cart.objects.get(id=cid)
        form = PlaceOrderForm(request.POST)
        if form.is_valid():
            address = form.cleaned_data.get("address")
            product = mobile
            order = Orders(address=address, product=product, user=request.user)
            order.save()
            cart.status = "orderplaced"
            cart.save()
            return redirect("user_home")
    return render(request, "placeorder.html", context)


@loginrequired
def my_orders(request, *args, **kwargs):
    ordered_items = Orders.objects.filter(user=request.user)
    cart_count = get_cart_count(request.user)
    context = {
        "ordered_items": ordered_items,
        "cart_count": cart_count
    }
    return render(request, "myorder.html", context)


def cancel_order(request,*args,**kwargs):
    oid = kwargs.get("id")
    order = Orders.objects.get(id=oid)
    order.status = "cancelled"
    order.save()
    return redirect("myorder")