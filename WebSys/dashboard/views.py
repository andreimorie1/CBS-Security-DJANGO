from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib.auth.models import User



# Create your views here.


@login_required
def index(request):
    orders = Order.objects.all()
    products = Product.objects.all()
    
    if request.POST:
        form = OrderForm(request.POST)
        if form.is_valid:
            instance = form.save(commit=False)
            instance.staff = request.user
            instance.save()
            messages.success()
            return redirect("dashboard:index")
    else:
        form = OrderForm()

    #topnav.html data counter
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        "form": form,
        "orders": orders,
        "products": products,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "products_count": products_count,
    }
    return render(request, "dashboard/index.html", context)


@login_required
def staff(request):
    workers = User.objects.all()
    
    #topnav.html data counter
    products_count = Product.objects.count()
    workers_count = workers.count()
    orders_count = Order.objects.all().count()
    context = {
        "workers": workers,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "products_count": products_count,
    }
    return render(request, "dashboard/staff.html", context)


@login_required
def staff_details(request, pk):
    workers = User.objects.get(id=pk)
    
    products_count = Product.objects.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        "workers": workers,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "products_count": products_count,
    }
    return render(request, "dashboard/staff_detail.html", context)


@login_required
def product(request):
    items = Product.objects.all()

    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            product_name = form.cleaned_data.get("name")
            messages.success(request, f"{product_name} Added to database")
            return redirect("dashboard:product")
    else:
        form = ProductForm()
        
    #topnav.html data counter
    products_count = items.count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        "items": items,
        "form": form,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "products_count": products_count,
    }
    return render(request, "dashboard/product.html", context)


@login_required
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect("dashboard:product")
    else:
        form = ProductForm(instance=item)
    context = {"form": form}
    return render(request, "dashboard/product_update.html", context)


@login_required
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == "POST":
        item.delete()
        return redirect("dashboard:product")
    return render(request, "dashboard/product_delete.html")


@login_required
def order(request):
    orders = Order.objects.all()
    
    #topnav.html counters
    products_count = Product.objects.all().count()
    workers_count = User.objects.all().count()
    orders_count = Order.objects.all().count()
    context = {
        "orders": orders,
        "workers_count": workers_count,
        "orders_count": orders_count,
        "products_count": products_count,
        }
    
    return render(request, "dashboard/order.html", context)
