from django.shortcuts import render
from django.http import HttpRequest
from django.contrib.auth import authenticate

from login.forms import LoginForm


# Create your views here.
def login(request: HttpRequest):

    login_form = LoginForm(request.POST)

    if login_form.is_valid():

        user = authenticate(
            request, username=login_form.username, password=login_form.password
        )

        if not user:
            login_form.add_error("username", "Usuario o contrasena incorrecta")
            login_form.add_error("password", "")

    else:
        login_form = LoginForm()

    return render(request, "login.html", {"form": login_form})
