from django.db import models

# Create your models here.

class Test(models.Model):
    
    name = models.CharField(max_length=200, verbose_name="用例名称")
    script_name = models.CharField(max_length=200, verbose_name='脚本名称')
    put_date = models.DateField(verbose_name="添加时间")



