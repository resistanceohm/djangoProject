"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from djangoProject.views import hello, today, today_proper, display, home, plot
from bookstore.views import add_author, all_authors, author_search
from bookstore.views import search_form, search

urlpatterns = [
    path('', home),
    path('plot/', plot),
    path('admin/', admin.site.urls),
    path('hello/', hello),
    path('today/', today_proper),
    path('display/', display),
    path('add_author/', add_author),
    path('authors/', all_authors),
    path('author_search/', author_search),
    path('search_form/', search_form),
    path('search/', search)
]
