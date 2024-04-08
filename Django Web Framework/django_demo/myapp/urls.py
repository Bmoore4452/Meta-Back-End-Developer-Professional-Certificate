from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("add/", views.add, name="add"),
    path("header/", views.header, name="header"),
    # path("getuser/<str:name>/<int:id>", views.pathview, name="pathview"),
    path("getuser/", views.pathview, name="pathview"),
    path("showform/", views.showform, name="showform"),
    path("showform/getform/", views.getform, name="getform"),
    path("menu/<str:dish>", views.menuitems, name="menuitems"),
]
