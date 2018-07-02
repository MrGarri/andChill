from django.http import HttpResponse
from django.contrib.auth import authenticate, login as user_login
from django.shortcuts import render, redirect
from django.template import loader


def index(request):
    return HttpResponse("Pelis y series aqui.")


def login(request):
    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    if username is not None:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect(index)

    template = loader.get_template("login/login.html")
    return HttpResponse(template.render({'username': username}, request))


def search(request):
    return HttpResponse("Mu bien")