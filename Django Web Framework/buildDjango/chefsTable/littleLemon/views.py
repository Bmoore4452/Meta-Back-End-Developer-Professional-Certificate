from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# from .models import Menu


def hello(request):
    return HttpResponse("Hello, Chef's Table!")


# def menu_by_id(request, menu_id):
#     menu = Menu.objects.get(pk=menu_id)
#     return HttpResponse(f"{menu.items}: Type of {menu.cuisine} cuisine")
