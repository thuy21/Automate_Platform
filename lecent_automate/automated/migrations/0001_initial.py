# Generated by Django 3.0 on 2020-06-17 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='用例名称')),
                ('script_name', models.CharField(max_length=200, verbose_name='脚本名称')),
                ('put_date', models.DateField(verbose_name='添加时间')),
            ],
        ),
    ]
