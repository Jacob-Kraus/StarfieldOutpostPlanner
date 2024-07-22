from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="StarfieldOutpostPlanner"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("home", views.home, name="home")
]
