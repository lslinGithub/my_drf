from django.urls import path, include
from . import views

# 路由
# game_list = views.GameView.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# game_detail = views.GameView.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
#  # path('games/', game_list, name='game-list'),  # 获取或创建
#  # path('games/<int:pk>/', game_detail, name='game-detail'),  # 查找、更新、删除

urlpatterns = [
    path('games6/', views.GameList.as_view(), name='game-list'),
    path('games6/<int:pk>/', views.GameDetail.as_view(), name='game-detail'),
    path('parsers/', views.ParserView.as_view(), name='parsers')
]
# 放在app路由下，实现url后缀
# from rest_framework.urlpatterns import format_suffix_patterns
#
# urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'api'])
# 使用router.register 就不需要写加后缀的定义，因为他已经实现了

# 上面方法适用于model 类视图，如果是API view
# def put(self, request, format=None, *args, **kwargs): # 这里只举例了一个视图

