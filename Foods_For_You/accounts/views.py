from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import LoginForm
# from accounts.auth import unauthenticated_user, admin_only,user_only
# from django.contrib.auth.decorators import login_required
# from meals.models import meals


def homepage(request):
    return render(request, 'accounts/homepage.html')

# @login_required
def logout_user(request):
    logout(request)
    return redirect('/login')

# @unauthenticated_user
def login_user(request):

    context={
        'form_login':LoginForm,
        'activate_login': 'active'
    }
    return render(request, 'accounts/login.html', context)


# @unauthenticated_user
def register_user(request):

    context={
        'form_register':UserCreationForm,
        'activate_register': 'active'

    }
    return render(request, 'accounts/register.html', context)


