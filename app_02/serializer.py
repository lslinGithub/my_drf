from django.conf import time
from rest_framework import serializers
from .models import Article, Category, Tag


# 最基本的序列化
class BaseArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True)
    num = serializers.IntegerField(required=True)
    content = serializers.CharField()

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    # instance为你要更新的实例，instance取不到就用原来的
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.num = validated_data.get('num', instance.num)
        instance.content = validated_data.get('content', instance.content)
        instance.save()
        return instance


# # 基本模型序列化
# class ModelArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'


# 基本模型序列化
# 1.serializers.StringRelatedField() # 以打印方式显示
# 2.serializers.PrimaryKeyRelatedField()
# 3.HyperlinkedRelatedField` requires the request in the serializer context.
# Add `context={'request': request}`
# category = serializers.HyperlinkedRelatedField(
#         view_name='app_02:category-detail', # 指定路由
#         read_only=True, # 不设置queryser,就设置read_only = True
#         # lookup_field='pk' # 查找字段，默认为pk，也就是路由写的字段参数
#     )
# 4.serializers.SlugRelatedField() # 将返回一个指定对应关系 model 中的字段，需要参数 slug_field 中指定字段名称。
# category = serializers.SlugRelatedField(
#         read_only=True,  # 不设置queryset,就设置read_only = True
#         slug_field='name' # 返回任意的模型字段名，跟StringRelatedField相似
#     )
# 5.serializers.HyperlinkedIdentityField( # 这个不用指明queryset
#         view_name='app_02:category-detail',
#         lookup_field='pk',
#     )

# class ModelArticleSerializer(serializers.ModelSerializer):
#     category = serializers.HyperlinkedIdentityField(
#         view_name='app_02:category-detail',
#         lookup_field='pk',
#     )
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = '__all__'

# 高级序列化
# 1.serializers.HyperlinkedModelSerializer
# class ModelArticleSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#         extra_kwargs = {
#             'url': {
#                 'view_name': 'app_02:article-detail',
#                 'lookup_field': 'pk'
#             },
#             'category': {
#                 'view_name': 'app_02:category-detail',
#                 'lookup_field': 'pk'
#             }
#         }
#
#
# class CategorySerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Category
#         fields = ('name', 'articles', 'url')
#
#         extra_kwargs = {
#             'url': {  # 如果写了fields = '__all__'字段，url默认代替id的位置.但要显示外键就要手写
#                 'view_name': 'app_02:category-detail',
#                 'lookup_field': 'pk'
#             },
#             'articles': {
#                 'view_name': 'app_02:article-detail',
#             }
#         }
# 2.序列化嵌套
# class ModelArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     articles = ModelArticleSerializer(many=True)
#
#     class Meta:
#         model = Category
#         fields = '__all__'

# 3.depth, 相当于嵌套序列化
# depth = 1
# 4.serializers.SerializerMethodField() # 实现特定方法
# count = serializers.SerializerMethodField()
#     class Meta:
#         model = Article
#         fields = ('id', 'title', 'num', 'content', 'category', 'count')
#     def get_count(self, obj):
#         return Article.objects.count()
# 5.source # 序列化指定的字段和字段来源 ，但只能读写，有特殊写法可实习读写，但是没有representation 好用
# category = serializers.CharField(source='category.name')
# arts = serializers.CharField(source="articles.id", ) # 反向查找莫名失败
# arts = serializers.CharField(source="articles.all", ) # get_xx_display
# class MyCharField(serializers.CharField):
#     def to_representation(self, value):
#         data_list = []  # 自定义返回
#         for val in value:
#             data_list.append({
#                 "title": val.title,
#                 "content": val.content
#             })
#         return data_list
#
#
# class ModelArticleSerializer(serializers.ModelSerializer):
#     category = serializers.CharField(source='category.name')
#
#     class Meta:
#         model = Article
#         fields = '__all__'
#
#
# class CategorySerializer(serializers.ModelSerializer):
#     arts = serializers.CharField(source="articles.all", )
#
#     class Meta:
#         model = Category
#         fields = ('id', 'name', 'arts')

# 6.    def to_representation(self, instance):
#         representation = super(ModelArticleSerializer, self).to_representation(instance)
#         representation['category'] = CategorySerializer(instance.category).data
#         representation['tags'] = TagSerializer(instance.tags, many=True).data
#         return representation
# 第6种以上的反序列化都有问题，而to_representation 只影响序列化
# created_time = serializers.DateTimeField(format='%Y-%m-%d') # 时间格式化
class ModelArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ModelArticleSerializer, self).to_representation(instance)
        representation['category'] = CategorySerializer(instance.category).data
        representation['tags'] = TagSerializer(instance.tags, many=True).data
        return representation


class CategorySerializer(serializers.ModelSerializer):
    articles = serializers.SlugRelatedField(
        slug_field='title',
        queryset=Article.objects.all(),
        many=True
    )

    class Meta:
        model = Category
        fields = ('id', 'name', 'articles')


class TagSerializer(serializers.ModelSerializer):
    created_time = serializers.DateTimeField(format='%Y-%m-%d %H:%M:%S')

    # def to_representation(self, instance):
    # to_representation时间格式化失败
    # representation = super(TagSerializer, self).to_representation(instance)
    # representation['created_time'] = TagSerializer(instance.created_time)
    # time_local = time.localtime(representation['created_time'])
    # print(time_local)
    # # representation['created_time'] = time_local.strftime('%Y-%m-%d %H:%m:%s')
    # return representation

    class Meta:
        model = Tag
        fields = ('id', 'name', 'created_time')
