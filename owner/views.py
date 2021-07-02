from django.shortcuts import render, redirect
from owner.forms import CreateBrandForm, ProductCreateForm
from .models import Brand, Product


# Create your views here.


def create_brand(request):
    if request.method == "GET":
        form = CreateBrandForm()
        context = {}
        context["form"] = form
        return render(request, 'createbrand.html', context)
    elif request.method == "POST":
        form = CreateBrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data.get("brand_name")
            brand = Brand(brand_name=brand_name)
            brand.save()
            print(brand_name)
            return render(request, 'createbrand.html')


def show_brand(request, id):
    brand = Brand.objects.get(id=id)
    context = {}
    context["brand"] = brand
    return render(request, 'showbrand.html', context)


def update_brand(request, id):
    brand = Brand.objects.get(id=id)
    dict = {"brand_name": brand.brand_name
            }
    form = CreateBrandForm(initial=dict)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = CreateBrandForm(request.POST)
        if form.is_valid():
            brand_name = form.cleaned_data.get("brand_name")
            brand.brand_name = brand_name
            brand.save()
            return redirect("show")
    return render(request, "editbrand.html", context)


def create_product(request):
    form = ProductCreateForm()
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreateForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
        else:
            context["form"] = form
            return render(request, "product_create.html", context)
    return render(request, "product_create.html", context)


def list_products(request):
    mobiles = Product.objects.all()
    context = {}
    context["mobiles"] = mobiles
    return render(request, "product_list.html", context)


def get_object(id):
    return Product.objects.get(id=id)


def edit_item(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id)
    form = ProductCreateForm(instance=product)
    context = {}
    context["form"] = form
    if request.method == "POST":
        form = ProductCreateForm(instance=product, data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("fetchitems")
    return render(request, "editproduct.html", context)


def product_details(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id)
    context = {}
    context["product"] = product
    return render(request, "item_detail.html", context)


def delete_product(request, *args, **kwargs):
    id = kwargs.get("id")
    product = get_object(id)
    product.delete()
    return redirect("fetchitems")


