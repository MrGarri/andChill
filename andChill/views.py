from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import authenticate, login as user_login
from django.shortcuts import render, redirect
from django.template import loader

from andChill.models import Movie

from andChill.api import find_movie


def index(request):
    if request.user.is_authenticated:
        return redirect(search)
    else:
        return redirect(login)


def login(request):
    if request.user.is_authenticated:
        return redirect(search)

    username = request.POST.get("username", None)
    password = request.POST.get("password", None)

    if username is not None:
        user = authenticate(request, username=username, password=password)
        if user is not None:
            user_login(request, user)
            return redirect(search)

    template = loader.get_template("login/login.html")
    return HttpResponse(template.render({'username': username}, request))


@login_required
def search(request):
    search_query = request.GET.get('search', '')
    movies = Movie.objects.filter(name__contains=search_query)
    template = loader.get_template("search/search.html")
    return HttpResponse(template.render({'movies': movies, 'search': search_query}, request))


@login_required
def watch(request, movie):
    queried_movie = Movie.objects.get(name=movie)

    movie_info = find_movie(queried_movie.name)

    for key, value in movie_info.items():
        if not queried_movie.__getattribute__(key):
            queried_movie.__setattr__(key, value)

    queried_movie.save()

    template = loader.get_template("watch/watch.html")
    return HttpResponse(template.render({'queried_movie': queried_movie}, request))
