from re import findall
from django.core.exceptions import MultipleObjectsReturned, ObjectDoesNotExist
from django.db import connection
from django.http import Http404, JsonResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
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
    tally = get_tally(request)
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'tally': tally})


def preowned(request, slug):  # a preowned homepage - populated with
    print('outpost_planner_app.views.preowned')
    matches = findall(r'_(\d+)-(\d+)+', slug)
    if not matches:
        print(f'matches: {matches}')
        print("BAD SLUG")
        return Http404  # TODO: slot in an error message instead of 404-ing
    cost_render = []
    row_data = []
    rows_render = list()
    for i, (om_id, num) in enumerate(matches):
        om_id = int(om_id)
        num = int(num)
        power = 0
        cost = []
        try:
            om = OutpostModule.objects.get(moduleID=om_id)
            rec = om.get_recipe()
            power = om.power * num
            ingredients = sorted(rec)
            cost = [f"{k}: {num * int(rec[k])}" for k in ingredients]
            row_data.append((num, om.name, rec, om.power))
        except (ObjectDoesNotExist, MultipleObjectsReturned):
            if int(om_id) != 0:
                print(f"Error looking up moduleID({om_id})")  # TODO: slot in an error message instead of 404-ing
                return Http404
            else:
                row_data.append((num, 0, {}, power))
                pass
        rows_render.append(
            render_to_string('outpost_selector.html',
                             {'modules': outpost_modules, 'rowIndex': i,
                              'moduleCount': num, 'moduleID': om_id, 'cost': cost, 'power': power},
                             request)
        )
    tally_render = get_tally(request, data=row_data)
    return render(request,
                  "home.html",
                  {"modules": outpost_modules, 'recipes': recipes,
                   'rows': rows_render, 'tally': tally_render})


def redirect_view(request):
    print('outpost_planner_app.views.redirect')
    print(f'    redirect_view(request): request.path_info: {request.path_info}')
    if 'home' in request.path_info:
        return redirect('home')
    return redirect('StarfieldOutpostPlanner')


def outpost_selector(request, row_index, module_count=0, module_id=0):
    print('outpost_planner_app.views.outpost_selector')
    return render(request,
                  "outpost_selector.html",
                  {'modules': outpost_modules, 'rowIndex': row_index,
                   'moduleCount': module_count, 'moduleID': module_id})


def module_cost_lookup(request, module_id):
    print('outpost_planner_app.views.module_cost_lookup')
    module_id = int(module_id)
    try:
        om = OutpostModule.objects.get(moduleID=module_id)
        rec = om.get_recipe()
        return JsonResponse(rec)
    except (ObjectDoesNotExist, MultipleObjectsReturned):
        print(f"Error looking up moduleID({module_id})")
        return Http404


def get_tally(request, data=None):
    print('outpost_planner_app.views.get_tally')
    if not data:
        data = []
    row_index = -1
    outpost_module_count = 0
    unique_outpost_modules = 0
    recipe_ingredients = 'NaN'
    power_value = 0
    u_modules = set()
    if len(data) > 0:
        recipe_ingredients = dict()
        for num, om_name, rec, power in data:
            outpost_module_count += int(num)
            u_modules.add(om_name)
            power_value += int(power) * int(num)
            try:
                for r_ingredient, r_count in rec.items():
                    if not recipe_ingredients.get(r_ingredient):
                        recipe_ingredients[r_ingredient] = 0
                    recipe_ingredients[r_ingredient] += int(r_count) * int(num)
            except ValueError:
                print(f"VALUE ERROR - rec: {rec}")
        resources = sorted(recipe_ingredients)
        recipe_ingredients = [f'{resource}: {recipe_ingredients[resource]}' for resource in resources]
        unique_outpost_modules = len(resources)
    return render_to_string('tally.html',
                            {'rowIndex': row_index,
                             'outpostModuleCountSum': outpost_module_count,
                             'uniqueOutpostModules': unique_outpost_modules,
                             'requiredResources': recipe_ingredients,
                             'powerValue': power_value},
                            request)
