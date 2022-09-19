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
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()  # 创建一个默认路由对象
# router.register(r'students', views.StudentViewsSet)  # 注册路由对象的路径，和绑定视图类
# router.register(r'groups', views.GroupViewSet)  # 注册路由对象的路径，和绑定视图类

urlpatterns = [
    # path('api/', include(router.urls))  # 创建完成的router对象使用include加入路由表
]

