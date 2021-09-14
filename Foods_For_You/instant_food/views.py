from django.shortcuts import render, redirect
from .forms import CatagoeryForm


class CategoryForm:
    pass


def Category_form(request):
    context ={
        'form_Category': CategoryForm,
        'active-Category': 'active'
    }
    return render(request, 'instant_food/Category_form.htm',context)

