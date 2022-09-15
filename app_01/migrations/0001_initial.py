# Generated by Django 4.1.1 on 2022-09-10 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=5, verbose_name='小组名字')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='学生名字')),
                ('age', models.IntegerField(verbose_name='学生年龄')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_01.group')),
            ],
        ),
    ]