from django.urls import path, re_path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/StarfieldOutpostPlanner/
    path(r"", views.index, name="StarfieldOutpostPlanner"),  # <root>/StarfieldOutpostPlanner/
    path(r"index", views.index, name="index"),
    re_path("home$", views.home, name="home"),
    path("home/<slug:slug>", views.preowned, name="preowned"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    #
    path("outpostSelector<int:row_index>", views.outpost_selector, name="outpostSelector"),
    path("costLookup<int:moduleID>", views.module_cost_lookup, name="costLookup"),
    path("tally", views.get_tally, name="tally"),
]
