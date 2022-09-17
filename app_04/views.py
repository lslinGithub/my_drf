from django.shortcuts import render
from rest_framework import viewsets
from .models import Game
from .serializer import GameSerializer


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # 方案一 重写perform_craate ,谁登录就是谁创建 ,但是更新PUT,PATCH 不行
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)