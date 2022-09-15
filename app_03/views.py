from rest_framework import mixins, generics
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializer import UserinfoSerializer
from .models import Userinfo
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class JsonResponse(HttpResponse):
    def __init__(self, *args, **kwargs):
        content = JSONRenderer().render(*args)
        kwargs['content_type'] = 'application/json'
        super(JsonResponse, self).__init__(content, **kwargs)


# 基于函数的视图
# @csrf_exempt
# def userinfo_list(request):
#     if request.method == 'GET':
#         users = Userinfo.objects.all()
#         ser = UserinfoSerializer(instance=users, many=True)
#         return JsonResponse(ser.data, status=200)
#     if request.method == "POST":
#         data = JSONParser().parse(request)
#         ser = UserinfoSerializer(data=data)
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=200)
#         return JsonResponse(ser.errors, status=400)
#
#
# @csrf_exempt
# def userinfo_detail(request, pk):
#     try:
#         user = Userinfo.objects.get(pk=pk)
#     except Userinfo.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         ser = UserinfoSerializer(instance=user)
#         return JsonResponse(ser.data, status=200)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         ser = UserinfoSerializer(instance=user, data=data)
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=201)
#         return JsonResponse(ser.errors, status=400)
#     elif request.method == "PATCH":
#         data = JSONParser().parse(request)
#         ser = UserinfoSerializer(instance=user, data=data)
#         if ser.is_valid():
#             ser.save()
#             return JsonResponse(ser.data, status=201)
#         return JsonResponse(ser.errors, status=400)
#     elif request.method == 'DELETE':
#         user.delete()
#         data = {
#             "data": "删除成功"
#         }
#         return JsonResponse(data, status=204)

# 基于装饰器的视图
@api_view(['GET', 'POST'])
def userinfo_list(request):
    if request.method == "GET":
        users = Userinfo.objects.all()
        ser = UserinfoSerializer(instance=users, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)
    if request.method == "POST":
        # 不需要JSONParser了,无论是装饰器还是类视图request和Response都是rest framework封装新的
        ser = UserinfoSerializer(data=request.data)  # 封装成功，直接request.data
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_200_OK)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
def userinfo_detail(request, pk):
    try:
        user = Userinfo.objects.get(pk=pk)
    except Userinfo.DoesNotExist:
        raise Http404("没有该对象")
    if request.method == "GET":
        ser = UserinfoSerializer(instance=user)
        return Response(ser.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        ser = UserinfoSerializer(instance=user, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "PATCH":
        ser = UserinfoSerializer(instance=user, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == "DELETE":
        user.delete()
        data = {
            "data": "删除成功"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


# 基于手写方法类的视图
class UserDetail(APIView):
    def get_object(self, pk):
        try:
            user = Userinfo.objects.get(pk=pk)
            return user
        except Userinfo.DoesNotExist:
            raise Http404()

    def get(self, request, *args, **kwargs):
        user = self.get_object(pk=kwargs.get('pk'))
        ser = UserinfoSerializer(instance=user)
        return Response(ser.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        user = self.get_object(pk=kwargs.get('pk'))
        ser = UserinfoSerializer(instance=user, data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('pk'))
        ser = UserinfoSerializer(instance=user, data=request.data, partial=True)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_201_CREATED)

    def delete(self, request, *args, **kwargs):
        user = self.get_object(kwargs.get('pk'))
        user.delete()
        data = {
            "data": "删除成功"
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        user = Userinfo.objects.all()
        ser = UserinfoSerializer(instance=user, many=True)
        return Response(ser.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        ser = UserinfoSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.data, status=status.HTTP_400_BAD_REQUEST)


# 基于mixin视图
# class UserList(mixins.ListModelMixin,  # 对应get.all()
#                mixins.CreateModelMixin,  # 对应POST提交， create
#                generics.GenericAPIView):  # 公用基础类
#     queryset = Userinfo.objects.all()  # 公用基础类指定需要序列化的queryset
#     serializer_class = UserinfoSerializer  # 公用基础类指定序列化类
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
#
# class UserDetial(mixins.RetrieveModelMixin,  # 对应get(pk='pk),查找一条数据
#                  mixins.UpdateModelMixin,  # 对应 PUT, PATCH
#                  mixins.DestroyModelMixin,  # 对应 DELETE
#                  generics.GenericAPIView):  # 公用基础类
#     queryset = Userinfo.objects.all()  # 公用基础类指定queryset
#     serializer_class = UserinfoSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)  # retrieve 单个数据获取
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def patch(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)

#     第二种写法, 是一样的操作
#     def patch(self, request, *args, **kwargs):
#         return self.partial_update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)  # destory 单个数据删除

# 更加封装的通用视图类, 上面懂了这个就好理解
class UserList(generics.ListCreateAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Userinfo.objects.all()
    serializer_class = UserinfoSerializer

