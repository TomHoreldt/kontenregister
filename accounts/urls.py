from django.urls import path
from . import views

urlpatterns = [

    path("login/", views.login, name="login"),

    path("person/", views.person, name="person"),

    path("logout/", views.logout, name="logout"),


]