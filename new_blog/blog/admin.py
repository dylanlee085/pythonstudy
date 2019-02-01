# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import BlogArticles

# Register your models here.
#新建BlogArticlesAdmin 类
class BlogArticlesAdmin(admin.ModelAdmin):
    #在admin 页面显示哪几列
    list_display = ("title", "author", "publish")
    #在admin 页面过滤显示
    list_filter = ("publish", "author")
    #在admin页面搜索
    search_fields = ("title", "body")
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
#将BlogArticles 注册到admin
admin.site.register(BlogArticles, BlogArticlesAdmin)
