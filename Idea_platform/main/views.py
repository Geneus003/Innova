from django.shortcuts import render

# Create your views here.

def index(request):
  file = 'index.html'
  return render(request, 'main/' + file ,{"file": file})

def login(request):
  return render(request, 'main/login.html')

def reg(request):
  file = 'reg.html'
  return render(request, 'main/' + file ,{"file": file})

def add_project(request):
  return render(request, 'main/add_project.html')
