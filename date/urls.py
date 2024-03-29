"""
URL configuration for calender project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path,include
from .views import *
from . import views
from .views import Registerview,LoginView, UserView,BookView,BookCreate

urlpatterns = [
    path('register',Registerview.as_view()),
    path('login',LoginView.as_view()),
    path('user', UserView.as_view()),
    path('books', BookView.as_view()),
    path('book-create',BookCreate.as_view()),
    path('book/<int:pk>',views.get_item),
    path('book-update/<int:pk>',views.update_item),
    path('book-delete/<int:pk>',views.delete_items)

]
