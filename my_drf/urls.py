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
from rest_framework.routers import DefaultRouter
from app_01 import views as app_01_views

app_01_router = DefaultRouter()  # 创建一个默认路由对象
app_01_router.register('students', app_01_views.StudentViewsSet, basename='app_01:student-detail')  # 注册路由对象的路径，和绑定视图类
app_01_router.register('groups', app_01_views.GroupViewSet)  # 注册路由对象的路径，和绑定视图类

from rest_framework.documentation import include_docs_urls  # 自动生成接口文档

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('app_01.urls', 'app_01'), namespace='app_01')),
    path('', include(('app_02.urls', 'app_02'), namespace='app_02')),
    path('', include(('app_03.urls', 'app_03'), namespace='app_03')),
    path('', include(('app_04.urls', 'app_04'), namespace='app_04')),
    path('', include(('app_05.urls', 'app_05'), namespace='app_05')),
    path('<str:version>/', include(('app_06.urls', 'app_06'), namespace='app_06')),  # 版本管制
    path('api/', include(app_01_router.urls)),  # 创建完成的router对象使用include加入路由表
    # 遇见的问题是注册在根路由的router.urls才能实现完整Hyp...Serializer，不然要在Modelviewset中额外指定url参数

    path('docs/', include_docs_urls(title='测试平台接口文档'))  # 自动生成接口文档
]
