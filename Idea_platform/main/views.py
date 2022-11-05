from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Categories, Ideas, CustomUser, Commands, AuthorCommands
from .forms import register
from django.contrib.auth import logout
from datetime import datetime
from django.views.generic import DetailView
from django.core import serializers
from django.db.models import Max
from django.views.generic.list import ListView
from django.views.generic.base import View



# Create your views here.


def index(request):
    # if request.is_ajax():
    #     return JsonResponse({'data': Categories.objects.all()})
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return JsonResponse({'data': Categories.objects.all()})

    context = {'ideas': Ideas.objects.all(), 'cat': Categories.objects.all()}
    return render(request, 'main/index.html', context)

def ajax(request):
    """Проверка доступности логина"""
    data = serializers.serialize("json", Categories.objects.all())
    response = {
        'data': data,
        'host': request.get_host(),
    }
    return JsonResponse(response)

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
        return render(request, 'main/add_idea.html', context)


# @login_required
# def profile(request):
#     return render(request, 'main/profile.html')


@login_required
def logout_rec(request):
    logout(request)
    return HttpResponseRedirect('/')


def search(request):
    cats = request.GET.get("cats", 1).split(",")
    cats = list(map(int, cats))
    print(cats)
    context = {'ideas': Ideas.objects.filter(category_id__in=cats), 'cat': Categories.objects.all()}
    # request.
    # return HttpResponseRedirect('/search/?cats=1,16')
    return render(request, 'main/index.html', context)


class ideas(DetailView):
    model = Ideas
    template_name = "main/idea.html"
    context_object_name = 'ideas'


# class team(View):
#     model = Commands
#     template_name = "main/team.html"
#     context_object_name = 'team'

#     def get(self, request, pk):
#         print(pk)
#         data = CustomUser.objects.all()
#         print(data)
#         return render(request, "main/team.html", {"bbb": data})

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['AC'] = AuthorCommands.objects.all()
#         context['user2'] = CustomUser.objects.all()
#         context['user'] = CustomUser.objects.all()

#         print(context['AC'])
#         print(context['user'])

#         return context


class team(DetailView):
    model = Commands
    template_name = "main/team.html"
    context_object_name = 'team'

    def get_context_data(self, **kwargs):
        now_command_id = self.kwargs['pk']
        context = super().get_context_data()
        command_authors = AuthorCommands.objects.filter(command_id__in=[int(now_command_id)])
        all_data = []
        for i in CustomUser.objects.filter(id__in=command_authors).values():
            all_data.append([i["first_name"], i["last_name"], i["email"]])
        context["AC"] = all_data
        context['user'] = all_data

        print(context['AC'])
        print(context['user'])

        return context


# class team(ListView):
#     model = Commands
#     template_name = "main/team.html"
#     context_object_name = 'team'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data()
#         context['AC'] = AuthorCommands.objects.all()
#         context['user2'] = CustomUser.objects.all()
#         context['user'] = CustomUser.objects.all()

#         print(context['AC'])
#         print(context['user'])

#         return context


class profile(DetailView):
    model = CustomUser
    template_name = "main/profile.html"
    context_object_name = 'user'

    def post(self, request, *args, **kwargs):
        # print("-----------------------")

        AC = AuthorCommands()

        # print(request.user.id)
        # print(self.get_object().id)
        # print(AuthorCommands.objects.get(author_id = request.user.id))

        AC.author_id = CustomUser.objects.get(id = self.get_object().id)
        AC.command_id = AuthorCommands.objects.get(author_id = request.user.id).command_id
        # AC.command_id = Commands.objects.get(id=id)

        AC.save()
        return HttpResponseRedirect('/')

@login_required
def add_team(request):

    if request.method == 'POST':

        # print(request.POST.get('title'))
        # print(request.POST.get('description'))
        # print(request.POST.get('category'))
        # print(datetime.now())
        # print(context['cat'].get(name = request.POST.get('category')).id)
        # print(CustomUser.objects.get(id = request.user.id))
        # print(request.user.id)

        team = Commands()
        AC = AuthorCommands()

        team.name = request.POST.get('title')
        team.description = request.POST.get('description')
        # team.author = CustomUser.objects.get(id=request.user.id)
        team.save()
        id = Commands.objects.aggregate(Max('id'))['id__max']
        AC.author_id = CustomUser.objects.get(id=request.user.id)
        AC.command_id = Commands.objects.get(id=id)
        AC.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'main/add_team.html')

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
