import io

from django.shortcuts import render
from django.http.response import JsonResponse, HttpResponse
from .serializer import BaseArticleSerializer, ModelArticleSerializer, CategorySerializer, TagSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .models import Article, Category, Tag
from django.views.decorators.csrf import csrf_exempt


# 封装一下JsonResponse
class JsonResponse(HttpResponse):

    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = "application/json"
        super(JsonResponse, self).__init__(content, **kwargs)


# Create your views here.
@csrf_exempt
def base_serializer_article_list(request):
    # 反序列化
    if request.method == 'POST':
        print('POST')
        # data = [
        #     {
        #         "title": '西游记',
        #         "num": 10,
        #         "content": "fdsafhahf苏悟空"
        #     },
        #     {
        #         "title": '未来人类',
        #         "num": 100,
        #         "content": "未来人类就是吊"
        #     }
        # ]
        # data = io.BytesIO(request.body)
        data = JSONParser().parse(request)
        ser = BaseArticleSerializer(data=data)
        if ser.is_valid():
            ser.save()
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json', status=200)
        else:
            json_data = JSONRenderer().render(ser.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)

    # 序列化
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = BaseArticleSerializer(instance=arts, many=True)
        json_data = JSONRenderer().render(ser.data)
        return HttpResponse(json_data, content_type='application/json', status=200)


# 模型序列化
@csrf_exempt
def model_serializer_article_list(request):
    if request.method == 'GET':
        arts = Article.objects.all()
        ser = ModelArticleSerializer(instance=arts, many=True, context={'request': request})
        # json_data = JSONRenderer().render(ser.data)
        # return HttpResponse(json_data, content_type='application/json', status=200)
        return JsonResponse(ser.data, status=200)

    if request.method == 'POST':
        data = JSONParser().parse(request)  # 这里把request丢进去就行了
        ser = ModelArticleSerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            json_data = JSONRenderer().render(ser.data)
            return HttpResponse(json_data, content_type='application/json', status=200)
        else:
            json_data = JSONRenderer().render(ser.errors)
            return HttpResponse(json_data, content_type='application/json', status=400)


# 模型序列化 单个方法实现
@csrf_exempt
def model_serializer_article_detail(request, pk):
    try:
        art = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == "GET":
        ser = ModelArticleSerializer(instance=art, context={'request': request})
        return JsonResponse(ser.data, status=200)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = ModelArticleSerializer(instance=art, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = ModelArticleSerializer(instance=art, data=data, partial=True, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)

    elif request.method == 'DELETE':
        art.delete()
        data = {"data": "删除成功"}
        return JsonResponse(data, status=204)


@csrf_exempt
def category_list(request):
    if request.method == 'GET':
        cats = Category.objects.all()
        ser = CategorySerializer(instance=cats, many=True, context={'request': request})
        return JsonResponse(ser.data, status=200)
    if request.method == 'POST':
        data = JSONParser().parse(request)
        ser = CategorySerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200)
        return JsonResponse(ser.errors, status=400)


@csrf_exempt
def category_detail(request, pk):
    try:
        cat = Category.objects.get(pk=pk)
    except Category.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == 'GET':
        ser = CategorySerializer(instance=cat, context={'request': request})
        return JsonResponse(ser.data, status=200)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = CategorySerializer(instance=cat, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)
    elif request.method == 'PATCH':
        data = JSONParser().parse(request)
        ser = CategorySerializer(instance=cat, data=data, partial=True, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201)
        return JsonResponse(ser.errors, status=400)
    elif request.method == 'DELETE':
        data = {"data": "删除成功"}
        return JsonResponse(data, status=204)


@csrf_exempt
def tag_list(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        ser = TagSerializer(instance=tags, many=True, context={'request': request})
        return JsonResponse(ser.data, status=200)
    if request.method == "POST":
        data = JSONParser().parse(request)
        ser = TagSerializer(data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, )
        return JsonResponse(ser.errors, status=400)


@csrf_exempt
def tag_detail(request, pk):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return HttpResponse(status=404)
    if request.method == "GET":
        ser = TagSerializer(instance=tag, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=200, context={'request': request})
        return JsonResponse(ser.errors, status=400, context={'request': request})

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        ser = TagSerializer(instance=tag, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201, context={'request': request})
        return JsonResponse(ser.errors, status=400, context={'request': request})

    elif request.method == "PATCH":
        data = JSONParser().parse(request)
        ser = TagSerializer(instance=tag, data=data, context={'request': request})
        if ser.is_valid():
            ser.save()
            return JsonResponse(ser.data, status=201, context={'request': request})
        return JsonResponse(ser.errors, status=400, context={'request': request})

    elif request.method == "DELETE":
        tag.delete()
        data = {"data": "删除成功"}
        return JsonResponse(data, status=204)
