from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20, verbose_name='游戏名称')
    desc = models.CharField(max_length=30, verbose_name='描述')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='games')
