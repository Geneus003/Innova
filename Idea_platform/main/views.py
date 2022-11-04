from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Categories, Ideas, CustomUser
from .forms import register
from django.contrib.auth import logout
from datetime import datetime

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


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
    context = {'cat': Categories.objects.all()}
    if request.method == 'POST':

        # print(request.POST.get('title'))
        # print(request.POST.get('description'))
        # print(request.POST.get('category'))
        # print(datetime.now())
        # print(context['cat'].get(name = request.POST.get('category')).id)
        # print(CustomUser.objects.get(id = request.user.id))
        # print(request.user.id)

        ideas = Ideas()
        ideas.name = request.POST.get('title')
        ideas.description = request.POST.get('description')
        ideas.release_date = datetime.now()
        ideas.author = CustomUser.objects.get(id=request.user.id)
        ideas.category = context['cat'].get(name=request.POST.get('category'))
        ideas.save()
        return HttpResponseRedirect('/')
    else:
        print(context)
        return render(request, 'main/add_idea.html', context)


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
