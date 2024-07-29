from django.urls import path, re_path

from . import views

urlpatterns = [
    # http://127.0.0.1:8000/StarfieldOutpostPlanner/
    path("", views.home, name="StarfieldOutpostPlanner$"),
    # http://127.0.0.1:8000/StarfieldOutpostPlanner/?quantity=1&outpost_module=87
    re_path(r"\?((quantity=\d\d?)&(outpost_module=\d\d?\d?))+",
            views.outpost_modules_display,
            name="outpost_modules_display"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("home", views.home, name="home")
]
