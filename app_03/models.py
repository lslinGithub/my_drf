from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Userinfo(models.Model):
    GENDERS = (
        (0, '女'),
        (1, '男')
    )
    phone = models.CharField(max_length=13, verbose_name="手机号码")
    gender = models.IntegerField(choices=GENDERS, verbose_name='性别')
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name='userinfo')
