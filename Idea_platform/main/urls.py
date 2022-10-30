from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg', views.reg, name='reg'),
    path('login', views.login, name='login'),
    path('add_project', views.add_project, name='add_project'),
    # path('profile', views.profile, name='profile'),
]
