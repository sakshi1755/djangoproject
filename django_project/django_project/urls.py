"""django_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django_project import views

urlpatterns = [
    path('', views.homepage),
    path('admin/', admin.site.urls),
    path('aboutus', views.aboutUs),
    path('aboutdetails<int:detailid>', views.aboutdetails),
    

   # one can use use int, slug(gh-jkl), str and even nothing when we are not sure about the type in place of int
]
