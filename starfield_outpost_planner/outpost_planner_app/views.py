from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import OutpostModule, Recipe, Resource


def index(request):
    return HttpResponse("Hello, world. You're at the starfield_outpost_planner [index].")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def home(request):
    outpost_modules = OutpostModule.objects.all()
    recipes = Recipe.objects.all()
    resources = Resource.objects.all()
    return render(request,
                  "home.html",
                  {"modules": outpost_modules,"recipes": recipes, "resources": resources})


def redirect_view(request):
    response = redirect('/StarfieldOutpostPlanner/')
    return response
