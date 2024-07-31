from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from .models import OutpostModule, Recipe


def index(request):
    return HttpResponse("Hello, world. You're at the starfield_outpost_planner [index].")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def home(request):
    outpost_modules = OutpostModule.objects.all()
    # TODO: get render object back from outpost_modules_display.html
    #   pass it to render request for home.html
    sub_view = outpost_modules_display(request,
                                       num=int(request.GET['num']),
                                       omID=int(request.GET['omID']),
                                       outpost_modules=outpost_modules)
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, "subView": sub_view})


def outpost_modules_display(request, num, omID, outpost_modules):
    recipes = Recipe.objects.all()
    module_query = outpost_modules.get(moduleID=omID)
    # note: querying with .get() will throw an error if 0 or >1 results found
    recipe_query = recipes.get(recipeID=module_query.recipeID)
    if not recipe_query:
        raise RuntimeError(f"query found no result for recipeID={recipe_query.recipeID}")
    tally_required_resources = dict()
    for attr in dir(recipe_query):
        if not attr.startswith('required'):
            continue
        val = getattr(recipe_query, attr)
        if not val:
            continue
        attr_key = attr[8:]  # cut off the "required" part of the label
        tally_required_resources[attr_key] = num * int(val)
    return render_to_string("outpost_modules_display.html",
                            {"modules": outpost_modules, "recipes": recipes},
                            request)


def redirect_view(request):
    response = redirect('/StarfieldOutpostPlanner/')
    return response
