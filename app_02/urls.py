"""my_drf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from . import views

urlpatterns = [
    path('base_article/', views.base_serializer_article_list),
    path('model_article/', views.model_serializer_article_list),
    path('model_article/<int:pk>/', views.model_serializer_article_detail, name='article-detail'),
    path('category_list/', views.category_list),
    path('category_detail/<int:pk>/', views.category_detail, name='category-detail'),
    path('tag_list/', views.tag_list, name='tag-list'),
    path('tag_detail/<int:pk>/', views.tag_detail, name='tag-detail'),
]
