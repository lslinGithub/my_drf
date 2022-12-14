# Generated by Django 4.1.1 on 2022-09-14 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_03', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=13, verbose_name='手机号码')),
                ('gender', models.IntegerField(choices=[(0, '女'), (1, '男')], verbose_name='性别')),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET, related_name='userinfo', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
