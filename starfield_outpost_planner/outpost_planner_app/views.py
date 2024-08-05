from django.db import connection
from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import OutpostModule, Recipe


outpost_modules = OutpostModule.objects.all()
recipes = Recipe.objects.all()


def get_context_data():
    with connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT *
            FROM  outpost_planner_app__outpostmodule AS om
            JOIN outpost_planner_app__recipe AS r
            ON om.recipeID=r.recipeID;
            """
        )
        result = cursor.fetchall()
    return result


def index(request):
    return HttpResponse("Hello, world. You're at the starfield_outpost_planner [index].")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def home(request):
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'recipes': recipes})


def redirect_view(request):
    response = redirect('/StarfieldOutpostPlanner/')
    return response


def outpost_selector(request, row_index):
    return render(request,
                  "outpost_selector.html",
                  {'modules': outpost_modules, 'rowIndex': row_index})
