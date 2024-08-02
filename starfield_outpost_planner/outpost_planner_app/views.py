from django.db.models import ObjectDoesNotExist
from django.http import Http404, HttpResponse, HttpResponseRedirect
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
    recipes = Recipe.objects.all()
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'recipes': recipes})


# def resource_cost_display(request, num, omID, outpost_modules):
#     recipes = Recipe.objects.all()
#     if not num and omID:
#         return ""
#     try:
#         module_query = outpost_modules.get(moduleID=omID)
#     except ObjectDoesNotExist:
#         return Http404
#     try:
#         recipe_query = recipes.get(recipeID=module_query.recipeID)
#     except ObjectDoesNotExist:
#         return Http404
#     required_resource_names = [attr for attr in dir(recipe_query) if attr.startswith("required") and getattr(recipe_query, attr)]
#     required_resource_names.sort()
#     required_resources = ', '.join([f'{attr}:{getattr(recipe_query, attr)}' for attr in required_resource_names])
#     return required_resources


# def outpost_modules_itemization(request, num, omID, outpost_modules):
#     recipes = Recipe.objects.all()
#
#     context = {'module_name': 'n/a', "num": "0", 'power': "0", 'resources': ""}
#
#     if not (num and omID):
#         return render_to_string("outpost_modules_itemization.html",
#                                 context, request)
#     else:
#         num = int(num)
#         # note: querying with .get() will throw an error if 0 or >1 results found
#         module_query = outpost_modules.get(moduleID=omID)
#         recipe_query = recipes.get(recipeID=module_query.recipeID)
#
#         tally_required_resources = dict()
#         for attr in dir(recipe_query):
#             if not attr.startswith('required'):
#                 continue
#             val = getattr(recipe_query, attr)
#             if not val:
#                 continue
#             attr_key = attr[8:]  # cut off the "required" part of the label
#             tally_required_resources[attr_key] = num * int(val)
#
#         required_resources = ', '.join([f"{k}:{v}" for k, v in tally_required_resources.items()])
#         power_mag = num * int(module_query.power)
#         power = f"{power_mag}" if not power_mag else f"+{power_mag}"
#
#         return render_to_string("outpost_modules_itemization.html",
#                                 {'module_name': module_query.name, "num": num,
#                                  'power': power, 'resources': required_resources},
#                                 request)


def redirect_view(request):
    response = redirect('/StarfieldOutpostPlanner/')
    return response
