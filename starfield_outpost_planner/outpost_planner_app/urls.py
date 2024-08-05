from django.urls import path, re_path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/StarfieldOutpostPlanner/
    path("", views.home, name="StarfieldOutpostPlanner/$"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("outpostSelector<int:row_index>", views.outpost_selector, name="outpostSelector"),
]
