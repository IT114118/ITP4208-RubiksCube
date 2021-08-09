"""rubiks_cube URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.contrib.auth import views as auth_views
from myapp.views import *
from myapp.auth import register, signin

urlpatterns = [
    path('admin/', admin.site.urls),

    # home page
    path('', ViewModelPost.as_view(template_name='home.html'), name='home'),                                    # (3) list post

    # web pages (hard code)
    path('puzzles/', TemplateView.as_view(template_name='puzzles.html'), name='puzzles'),                       # (1) Introducing some puzzles;
    path('speedsolvers/', TemplateView.as_view(template_name='speedsolvers.html'), name='speedsolvers'),        # (2) Introducing some famous speedsolvers;
    path('solve3x3/', TemplateView.as_view(template_name='solve_cube.html'), name='solve_cube'),                # (3) Introducing how to solve the 3x3 cube;

    # the functions from lab11
    path('register/', register, name='register'),                                                               # (1) Able to register as a member;
    #path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),                     # (2) Able to log in your web application;
    path('login/', signin, name='login'),                                                                       # (2) Able to log in your web application;
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('post/manage/', ViewModelPost.as_view(template_name='models/post/manage.html'), name='post_manage'),   # (3) Able to create a post, delete a post, update post
    path('post/create/', CreateModelPost.as_view(), name='post_create'),
    path('post/update/<int:id>/', UpdateModelPost.as_view(), name='post_update'),
    path('post/delete/<int:pk>/', DeleteModelPost.as_view(), name='post_delete'),

    # new model 1
    path('3x3alg/', ViewModelAlgorithm.as_view(template_name='models/3x3alg/list.html'), name='alg_list'),
    path('3x3alg/manage/', ViewModelAlgorithm.as_view(template_name='models/3x3alg/manage.html'), name='alg_manage'),
    path('3x3alg/create/', CreateModelAlgorithm.as_view(), name='alg_create'),
    path('3x3alg/update/<int:id>/', UpdateModelAlgorithm.as_view(), name='alg_update'),
    path('3x3alg/delete/<int:pk>/', DeleteModelAlgorithm.as_view(), name='alg_delete'),

    # new model 2
    path('3x3pattern/', ViewModelPattern.as_view(template_name='models/3x3pattern/list.html'), name='pattern_list'),
    path('3x3pattern/manage/', ViewModelPattern.as_view(template_name='models/3x3pattern/manage.html'), name='pattern_manage'),
    path('3x3pattern/create/', CreateModelPattern.as_view(), name='pattern_create'),
    path('3x3pattern/update/<int:id>/', UpdateModelPattern.as_view(), name='pattern_update'),
    path('3x3pattern/delete/<int:pk>/', DeleteModelPattern.as_view(), name='pattern_delete'),
]
