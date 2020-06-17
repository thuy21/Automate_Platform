from django.contrib import admin
from .models import Test

# Register your models here.

@admin.register(Test)
class AutomatedAdmin(admin.ModelAdmin):

    search_fields = ['name', 'script_name'] # 根据字段名称进行查询
    list_display = ['name', 'script_name', 'put_date']  # 设置列表显示字段
    list_per_page = 20  #设置分页数据20条

admin.site.site_header = '测试平台'    # 设置header显示方式
admin.site.site_title = 'Web自动化测试平台'     # 设置title显示方式
