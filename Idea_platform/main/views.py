from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from .forms import register
from django.contrib.auth import logout

# Create your views here.

def index(request):
  return render(request, 'main/index.html')

def login(request):
  return render(request, 'main/login2.html')
  # print("-----------------------------" + request.method)
  # if request.method == "POST":
  #   email = request.POST.get("email")
  #   password = request.POST.get("password")

  #   users = CustomUser.objects.all()
  #   users = users.filter(email = email)

  #   print(request.POST.get("name"))
  #   print(len(users))
  #   print(users.exists())
  #   if (len(users) > 0):
  #     for user in users:
  #       print(f"{user.id}.{user.first_name} -- {user.email}")

  #   if (users.exists()):
  #     return HttpResponseRedirect("/")
  #   else:
  #     return render(request, 'main/login2.html', {"fail": 'Неправильная поста или пароль.'})
  # else:
  #   return render(request, 'main/login2.html')


def reg(request):
  if request.method == 'POST':
    user_form = register(request.POST)
    if user_form.is_valid():
      print("+++++++++++++++++++++++++++++++++++++=")
      # Create a new user object but avoid saving it yet
      new_user = user_form.save(commit=False)
      # Set the chosen password
      new_user.set_password(user_form.cleaned_data['password'])
      # Save the User object
      new_user.save()
      return render(request, 'main/login.html', {'new_user': new_user})
    else:
      print("--------------------------------------")
  else:
    user_form = register()
  return render(request, 'main/reg.html', {'user_form': user_form})
 

@login_required
def add_idea(request):
  if request.method == 'POST':
    print(request.POST.get('title'))
    print(request.POST.get('description'))
    print(request.POST.get('category'))
    return HttpResponseRedirect('/')
  else:
    return render(request, 'main/add_idea.html')

@login_required
def profile(request):
  return render(request, 'main/profile.html')

def logout_rec(request):
  logout(request)
  return HttpResponseRedirect('/')


# # сохранение данных в бд
# def create(request):
#     if request.method == "POST":
#         user = Users2()
#         user.name = request.POST.get("name")
#         user.age = request.POST.get("age")
#         user.save()
#     return HttpResponseRedirect("/")
 
# # изменение данных в бд
# def edit(request, id):
#     try:
#         user = Users2.objects.get(id=id)
 
#         if request.method == "POST":
#             user.name = request.POST.get("name")
#             user.age = request.POST.get("age")
#             user.save()
#             return HttpResponseRedirect("/")
#         else:
#             return render(request, "edit.html", {"user": user})
#     except Users2.DoesNotExist:
#         return HttpResponseNotFound("<h2>user not found</h2>")
     
# # удаление данных из бд
# def delete(request, id):
#     try:
#         user = Users2.objects.get(id=id)
#         user.delete()
#         return HttpResponseRedirect("/")
#     except Users2.DoesNotExist:
#         return HttpResponseNotFound("<h2>user not found</h2>")