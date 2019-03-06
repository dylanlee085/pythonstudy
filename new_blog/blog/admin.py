# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib import admin
from .models import BlogArticles
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Register your models here.

class BlogArticlesAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publish")
    list_filter = ("publish", "author")
    search_fields = ("title", "body")
#列表中只有一个返回项时需要加入逗号识别
    raw_id_fields = ("author",)
    date_hierarchy = "publish"
    ordering = ["publish", "author"]

admin.site.register(BlogArticles, BlogArticlesAdmin)
