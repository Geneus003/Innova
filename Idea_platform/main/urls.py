from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('reg', views.reg, name='reg'),
    # path('login/', views.login, name='login'),
    path('add_idea', views.add_idea, name='add_idea'),
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('profile', views.profile, name='profile'),
]

urlpatterns += [
    # path('', include('django.contrib.auth.urls')),
    # path('/', include('django.contrib.auth.urls')),
]