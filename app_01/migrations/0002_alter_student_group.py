# Generated by Django 4.1.1 on 2022-09-10 14:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_01', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student', to='app_01.group', verbose_name='小组'),
        ),
    ]
