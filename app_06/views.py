from django.http import HttpResponse
from django.shortcuts import render
from rest_framework import generics
from .models import Game
from .serializers import GameSerializer
from rest_framework.views import APIView


# Create your views here.
class GameList(generics.ListCreateAPIView):
    # queryset = Game.objects.all()
    serializer_class = GameSerializer

    # pagination_class = (,)

    # 重写get_queryset,get_serializer实现不同版本控制
    def get_queryset(self):
        if self.request.version == 'v1':
            queryset = Game.objects.filter(status=0)
        elif self.request.version == 'v2':
            queryset = Game.objects.filter(status=1)
        return queryset
    # def get_serializer_class(self):


class GameDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer


# 解析器
from rest_framework.parsers import FormParser, JSONParser, FileUploadParser, MultiPartParser


class ParserView(APIView):
    # parser_classes = []

    def post(self, request, *args, **kwargs):
        # print("body:", request.body.decode())
        print("content_type:", request.content_type)
        # 获取请求的值，并使用对应的JSONParser进行处理
        print("data:", request.data)
        # application/x-www-form-urlencoded 或 multipart/form-data时，request.POST中才有值
        print("POST:", request.POST)
        print("FILES:", request.FILES)

        return HttpResponse('响应')
