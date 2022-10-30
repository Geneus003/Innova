from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def auth_function(request):
    template = loader.get_template('auth/login.html')
    context = None
    return HttpResponse(template.render(context, request))
