from rest_framework import serializers
from .models import Game
from rest_framework import permissions
from .permissions import IsOwnerOrReadOnly


class GameSerializer(serializers.ModelSerializer):
    # 方案二 HiddenFiled ,谁登录就是谁创建, 失败, 不好用
    # user = serializers.CurrentUserDefault()
    # 权限需要更多了解，所看课程内容太简短

    # 加入自己写的权限
    permission_class = [permissions.IsAuthenticated, IsOwnerOrReadOnly]

    class Meta:
        model = Game
        fields = '__all__'

        # exclude = ('user',)
        # extra_kwargs = {
        #     "user": {
        #         "read_only": True
        #     }
        # }
