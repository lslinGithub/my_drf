import re

from rest_framework import serializers
from .models import Userinfo


class UserinfoSerializer(serializers.ModelSerializer):
    # phone = serializers.CharField(required=True)

    class Meta:
        model = Userinfo
        fields = ('phone', 'gender', 'user')

    # 自定义验证
    def validate_phone(self, phone):
        if not re.match(r'1[3456789]\d{9}', phone):
            raise serializers.ValidationError('手机号不合法')
        if Userinfo.objects.filter(phone=phone).all():
            raise serializers.ValidationError('手机号已被注册')
        return phone  # 一定要有返回值

    # 加密密码需要重写create 方法

    # 联合验证时，重写validate
    # 两次密码是否一样
    # def validate(self, attrs):
    #     print(attrs)
    #     if attrs['pwd'] != attrs['pwd1']:
    #         raise serializers.ValidationError('两次密码不一样')
    #     return attrs
