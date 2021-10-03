from django.shortcuts import render, redirect
from .forms import CatagoeryForm, MealsForm , OrderForm
from django.contrib import messages

from .models import Catagoery, Meals, Cart, Order

from accounts.auth import admin_only, user_only
from django.contrib.auth.decorators import login_required
import os

def homepage(request):
    return render(request, 'meals/homepage.html')

@login_required
@admin_only
def catagoery_form(request):
    if request.method == "POST":
        form = CatagoeryForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Catagoery added successfully')
            return redirect("/meals/get_catagoery")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add catagoery')
            return render(request, 'meals/catagoery_form.html', {'catagoery_form': form})


    context ={
        'catagoery_form': CatagoeryForm,
        'activate_catagoery': 'active'

    }
    return render(request, 'meals/catagoery_form.html', context)

@login_required
@admin_only
def get_catagoery(request):
    categories =  Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_catagoery':'active'
    }
    return render(request, 'meals/get_catagoery.html', context)


@login_required
@admin_only
def delete_catagoery(request, catagoery_id):
    catagoery = Catagoery.objects.get(id=catagoery_id)
    catagoery.delete()
    messages.add_message(request, messages.SUCCESS, 'Catagoery Deleted Successfully')
    return redirect('/meals/get_catagoery')

def catagoery_update_form(request, catagoery_id):
    catagoery = Catagoery.objects.get(id=catagoery_id)
    if request.method == "POST":
        form = CatagoeryForm(request.POST,instance=catagoery)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Catagoery updated successfully')
            return redirect("/meals/get_catagoery")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update catagoery')
            return render(request, 'meals/catagoery_update_form.html', {'catagoery_form':form})
    context ={
        'form_catagoery': CatagoeryForm(instance=catagoery),
        'activate_catagoery': 'active'
    }
    return render(request, 'meals/catagoery_update_form.html', context)

@login_required
@admin_only
def meals_form(request):
    if request.method == "POST":
        form = MealsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Meals added successfully')
            return redirect("/meals/get_meals")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add meals')
            return render(request, 'meals/meals_form.html', {'meals_form':form})
    context ={
        'meals_form': MealsForm,
        'activate_meals': 'active'
    }
    return render(request, 'meals/meals_form.html', context)

@login_required
@admin_only
def get_meals(request):
    meals =  Meals.objects.all().order_by('-id')
    context = {
        'meals':meals,
        'activate_meals':'active'
    }
    return render(request, 'meals/get_meals.html', context)

@login_required
@admin_only
def delete_meals(request, meals_id):
    meals = Meals.objects.get(id=meals_id)
    os.remove(meals.meals_image.path)
    meals.delete()
    messages.add_message(request, messages.SUCCESS, 'Meals Deleted Successfully')
    return redirect('/meals/get_meals')


@login_required
@admin_only
def meals_update_form(request, meals_id):
    meals = Meals.objects.get(id=meals_id)
    if request.method == "POST":
        if request.FILES.get('meals_image'):
            os.remove(meals.meals_image.path)
        form = meals_form(request.POST, request.FILES, instance=meals)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Meals updated successfully')
            return redirect("/meals/get_meals")
        else:
            messages.add_message(request, messages.ERROR, 'Unable to update food')
            return render(request, 'meals/meals_form.html', {'meals_form':form})
    context ={
        'meals_form': meals_form(instance=meals),
        'activate_meals': 'active'
    }
    return render(request, 'meals/meals_update_form.html', context)

def show_categories(request):
    categories = Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_catagoery_user': 'active'
    }
    return render(request, 'meals/show_categories.html', context)

def show_meals(request):
    meals = Meals.objects.all().order_by('-id')
    context = {
        'meals':meals,
        'activate_meals_user': 'active'
    }
    return render(request, 'meals/show_meals.html', context)

def menu(request):
    categories  = Catagoery.objects.all().order_by('-id')
    context = {
        'categories':categories,
        'activate_menu':'active'
    }
    return render(request, 'meals/menu.html', context)


@login_required
@user_only
def add_to_cart(request, meals_id):
    user = request.user
    meals = Meals.objects.get(id=meals_id)

    check_item_presence = Cart.objects.filter(user=user, meals=meals)
    if check_item_presence:
        messages.add_message(request, messages.ERROR, 'Item is already added.')
        return redirect('/meals/get_meals_user')
    else:
        cart = Cart.objects.create(meals=meals, user=user)
        if cart:
            messages.add_message(request, messages.SUCCESS, 'Item added to cart')
            return redirect('/meals/mycart')
        else:
            messages.add_message(request, messages.ERROR, 'Unable to add item to cart')
@login_required
@user_only
def show_cart_items(request):
    user = request.user
    items = Cart.objects.filter(user= user)
    context = {
        'items':items,
        'activate_my_cart':'active'
    }
    return render(request, 'meals/mycart.html', context)
@login_required
@user_only
def remove_cart_item(request, cart_id):
    item = Cart.objects.get(id=cart_id)
    item.delete()
    messages.add_message(request, messages.SUCCESS, 'Item was deleted successfully from cart')
    return redirect('/meals/mycart')
@login_required
@user_only





def order_form(request, meals_id, cart_id, meals=None):
    user = request.user
    meals = meals.objects.get(id=meals_id)
    cart_item = Cart.objects.get(id=cart_id)
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            quantity = request.POST.get('quantity')
            price = meals.meals_price
            total_price = int(quantity)*int(price)
            contact_no = request.POST.get('contact_no')
            contact_address = request.POST.get('contact_address')
            payment_method = request.POST.get('payment_method')
            order = Order.objects.create(meals=meals,
                                         user =user,
                                         quantity=quantity,
                                         total_price=total_price,
                                         contact_no = contact_no,
                                         contact_address =contact_address,
                                         status="Pending",
                                         payment_method= payment_method,
                                         payment_status=False
            )
            if order:
                context = {
                    'order':order,
                    'cart':cart_item
                }
                return render(request, 'meals/esewa_payment.html', context)
        else:
            messages.add_message(request, messages.ERROR, 'Something went wrong')
            return render(request, 'meals/order_form.html', {'order_form':form})
    context = {
        'order_form': OrderForm
    }
    return render(request, 'meals/order_form.html', context)

# import request as req
def esewa_verify(request):
    import xml.etree.ElementTree as ET
    o_id = request.GET.get('oid')
    amount = request.GET.get('amt')
    refId = request.GET.get('refId')
    url = "https://uat.esewa.com.np/epay/transrec"
    d = {
        'amt': amount,
        'scd': 'EPAYTEST',
        'rid': refId,
        'pid': o_id,
    }
    resp = request.post(url, d)
    root = ET.fromstring(resp.content)
    status = root[0].text.strip()
    if status == 'Success':
        order_id = o_id.split("_")[0]
        order = Order.objects.get(id=order_id)
        order.payment_status = True
        order.save()
        cart_id = o_id.split("_")[1]
        cart = Cart.objects.get(id=cart_id)
        cart.delete()
        messages.add_message(request, messages.SUCCESS, 'Payment Successful')
        return redirect('/meals/mycart')
    else:
        messages.add_message(request, messages.ERROR, 'Unable to make payment')
        return redirect('/meals/mycart')



@login_required
@user_only
def my_order(request):
    user = request.user
    items = Order.objects.filter(user=user).order_by('-id')
    context = {
        'items':items,
        'activate_myorders':'active'
    }
    return render(request, 'meals/my_order.html', context)















