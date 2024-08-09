import re
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import connection
from django.http import Http404, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import OutpostModule, Recipe


outpost_modules = OutpostModule.objects.all()
recipes = Recipe.objects.all()
host = 'http://127.0.0.1:8000/'  # TODO: change when not hosting locally
# host = http://127.0.0.1:8000/


def get_context_data():
    print('outpost_planner_app.views.get_context_data')
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
    # return HttpResponse("Hello, world. You're at the starfield_outpost_planner [index].")
    return render(request, "index.html", {'host': host})


def about(request):
    print('outpost_planner_app.views.about')
    return render(request, "about.html", {'host': host})


def contact(request):
    print('outpost_planner_app.views.contact')
    return render(request, "contact.html", {'host': host})


def home(request):
    print('outpost_planner_app.views.home')
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'recipes': recipes, 'host': host})


def preowned(request, slug):
    print('outpost_planner_app.views.preowned')
    matches = re.findall(r'_(\d+)-(\d+)+', slug)
    if not matches:
        print("BAD SLUG")
        return Http404  # TODO: return to home, with error message displayed
    outpost_slugs = {}
    for k, v in matches:
        outpost_slugs[int(k)] = int(v)
    slugs = list(outpost_slugs.keys())
    slugs.sort()
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'recipes': recipes, 'host': host,
                           'outpost_slugs': outpost_slugs, 'slugs': slugs})


def redirect_view(request):
    print('outpost_planner_app.views.redirect')
    response = redirect('StarfieldOutpostPlanner')
    return response


def outpost_selector(request, row_index):
    print('outpost_planner_app.views.outpost_selector')
    return render(request,
                  "outpost_selector.html",
                  {'modules': outpost_modules, 'rowIndex': row_index})


def module_cost_lookup(request, moduleID):
    print('outpost_planner_app.views.module_cost_lookup')
    moduleID = int(moduleID)
    try:
        om = OutpostModule.objects.get(moduleID=moduleID)
        rec = om.get_recipe()
        return JsonResponse(rec)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        print(f"Error looking up moduleID({moduleID})")
        return Http404
