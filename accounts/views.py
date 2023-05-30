from django.shortcuts import render, redirect
from yangpt_app.models import User
from django.contrib import auth


def login(request):
    if request.method == "POST":
        return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
