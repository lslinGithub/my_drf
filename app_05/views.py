from django.http import JsonResponse
from rest_framework.authentication import BasicAuthentication, TokenAuthentication, SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.views import APIView
from .throttlings import VisitThrottle


# Create your views here.

class CarsView(APIView):
    # 基于什么认证的，
    authentication_classes = [JSONWebTokenAuthentication]

    # 权限
    permission_classes = [IsAuthenticated]

    # 节流
    throttle_classes = [VisitThrottle]

    # 版本
    versioning_class = ()

    # 分页
    # pagination_class = ()

    # 解析器
    # parser_classes = []
    def get(self, request, *args, **kwargs):
        ctx = {
            "code": 1,
            "msg": "ok",
            "data": {
                "goods": {
                    "name": "苹果",
                    "price": 12
                }
            }
        }
        return JsonResponse(ctx)


# 自定义认证
# from rest_framework.views import APIView
# from .models import User, UserToken
# import hashlib
# import time
# from django.http import JsonResponse
#
#
# def get_md5(user):
#     ctime = str(time.time())
#     m = hashlib.md5(bytes(user, encoding='utf-8'))
#     m.update(bytes(ctime, encoding='utf-8'))
#     return m.hexdigest()
#
# 创建token的视图
# class AuthView(APIView):
#     def post(self, request):
#         ret = {'code': 1, 'msg': None, 'data': {}}
#         user = request._request.POST.get('username')
#         pwd = request._request.POST.get('password')
#         obj = User.objects.filter(username=user, password=pwd).first()
#         if not obj:
#             ret['code'] = -1
#             ret['msg'] = "用户名或密码错误"
#         token = get_md5(user)
#         UserToken.objects.update_or_create(user=obj, defaults={'token': token})
#         ret['token'] = token
#         return JsonResponse(ret)
#
#
# from rest_framework import exceptions
# from rest_framework.authentication import BaseAuthentication
#
#
# class Authtication(BaseAuthentication):
#     def authenticate(self, request):
#         '''
#         header key必须大写，前缀必须是"HTTP",后面如果连接符是横线“-”，要改成下划线“_”。例如你的header的key为api_auth，那在Django中应该使用request.META.get("HTTP_API_AUTH")来获取请求头的数据。
#         '''
#         token = request.META.get('HTTP_TOKEN')  # META 是请求头
#
#     obj = UserToken.objects.filter(token=token).first()
#     if not obj:
#         raise exceptions.AuthenticationFailed('用户认证失败')
#     return (obj.user, obj)

class VersionView(APIView):
    def get(self, request, *args, **kwargs):
        print(request.version)
        if request.version == 'v1':
            ctx = {
                "code": 1,
                "msg": "ok",
                "data": {}
            }
            return JsonResponse(ctx)
        elif request.version == 'v2':
            ctx = {
                "code": 2,
                "msg": "ok",
                "data": {}
            }
            # 获取版本
            print(request.version)
            # 获取版本管理的类
            print(request.versioning_scheme)
            # 反向生成URL
            reverse_url = request.versioning_scheme.reverse('app_05:version-view', request=request)
            print(reverse_url)
            return JsonResponse(ctx)



