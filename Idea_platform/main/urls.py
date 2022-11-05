from django.urls import path, include, re_path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg/', views.reg, name='reg'),
    # path('login/', views.login, name='login'),
    path('add_idea/', views.add_idea, name='add_idea'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    # path('profile/', views.profile, name='profile'),
    path('logout', views.logout_rec, name='logout'),
    path('idea/<int:pk>', views.ideas.as_view(), name='ideas'),
    path('search/', views.search, name="search"),
    # path('team', views.team, name='team'),
    path('ajax', views.ajax, name='ajax'),
    path('profile/<int:pk>', login_required(views.profile.as_view()), name='profile'),
    path('team/<int:pk>', login_required(views.team.as_view()), name='team'),
    path('add_team', views.add_team, name='add_team'),
]
