from django.shortcuts import render

# Create your views here.
from .custom_model_view_set import CustomModelViewSet


# 利用queryset 来过滤
# http://127.0.0.1:8000/api/v1/games/?ordering=-id
class GameView(CustomModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    def get_queryset(self):
        ordering = self.request.query_params.get('ordering')
        if not ordering:
            queryset = Game.objects.all()
        else:
            queryset = Game.objects.all().order_by(ordering)
        return queryset


# 利用filter 库来过滤 pip install django-filter

INSTALLED_APPS = [
    """"""
    django_filters,
]
# 全局配置
'DEFAULT_FILTER_BACKENDS': (
    'django_filters.rest_framework.DjangoFilterBackend',
    ...
),

from .custom_model_view_set import CustomModelViewSet
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend


class GameView(CustomModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer
    # 局部生效
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('name', 'status')


# http://127.0.0.1:8000/api/v1/games/?status=1&name=和平精英
# 不支持模糊搜索
# 自定义过滤类
from .custom_model_view_set import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filter import GameFilter


class GameView(CustomModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = (DjangoFilterBackend,)
    # filter_fields = ('name', 'status')
    filterset_class = GameFilter


# 搜索
from .custom_model_view_set import CustomModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from .custom_filter import GameFilter
from rest_framework import filters


class GameView(CustomModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)

    # 过滤
    filter_fields = ('name', 'status')
    filterset_class = GameFilter

    # 搜索
    search_fields = ("name", "status")

    # http://127.0.0.1:8000/api/v1/games/?search = 天

# 排序
class GameView(CustomModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)

    # 过滤
    # filter_fields = ('name', 'status')
    filterset_class = GameFilter

    # 搜索
    search_fields = ("name", "status")

    # 排序
    # 注意 filter_backends多了一个filters.OrderingFilter
    ordering_fields = ['status', "id", "name"]

