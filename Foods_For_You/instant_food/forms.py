from django import forms
from django.forms import ModelForm

from .models import Catagoery

class CatagoeryForm(ModelForm):
    class Meta:
        model = Catagoery
        fields = "__all__"



class FoodForm(ModelForm):
    class Meta:
        model = Food
        fields = "__all__"


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['quantity', 'contact_no', 'contact_address', 'payment_method']
