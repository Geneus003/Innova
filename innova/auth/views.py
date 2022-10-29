from django.shortcuts import render
from django.http import HttpResponse


def auth_function(request):
    return HttpResponse("Страница приложения")
