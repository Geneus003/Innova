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
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return HttpResponseRedirect('../login')
    else:
        user_form = register()
    return render(request, 'main/reg.html', {'user_form': user_form})
 

@login_required
def add_idea(request):
    context = {'cat': Categories.objects.all()}
    if request.method == 'POST':


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


@login_required
def logout_rec(request):
    logout(request)
    return HttpResponseRedirect('/')


def search(request):
    cats = request.GET.get("cats", 1).split(",")
    cats = list(map(int, cats))
    context = {'ideas': Ideas.objects.filter(category_id__in=cats), 'cat': Categories.objects.all()}
    return render(request, 'main/index.html', context)


class ideas(DetailView):
    model = Ideas
    template_name = "main/idea.html"
    context_object_name = 'ideas'


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

        return context


class profile(DetailView):
    model = CustomUser
    template_name = "main/profile.html"
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        now_command_id = self.kwargs['pk']
        context = super().get_context_data()
        c_a = AuthorCommands.objects.filter(author_id=self.request.user.id).values()
        command_ids = []
        for i in c_a:
            command_ids.append(i["command_id_id"])
        all_data = []
        data=[]

        ideas = Ideas.objects.filter(author_id = now_command_id)
        context['ideas'] = ideas

        for i in Commands.objects.filter(id__in=command_ids).values():
            data.append(i)
            all_data.append([i["name"], i["id"]])

        context['c_a'] = c_a
        context['teams'] = data

        return context

    def post(self, request, *args, **kwargs):

        AC = AuthorCommands()

        AC.author_id = CustomUser.objects.get(id = self.get_object().id)
        AC.command_id = AuthorCommands.objects.get(author_id = request.user.id).command_id

        AC.save()
        return HttpResponseRedirect('/')

@login_required
def add_team(request):

    if request.method == 'POST':

        team = Commands()
        AC = AuthorCommands()

        team.name = request.POST.get('title')
        team.description = request.POST.get('description')
        team.save()
        id = Commands.objects.aggregate(Max('id'))['id__max']
        AC.author_id = CustomUser.objects.get(id=request.user.id)
        AC.command_id = Commands.objects.get(id=id)
        AC.save()
        return HttpResponseRedirect('/')
    else:
        return render(request, 'main/add_team.html')

def users(request):
    return render(request, 'main/users.html', {'users': CustomUser.objects.all()})