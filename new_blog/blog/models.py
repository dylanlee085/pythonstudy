# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
#导入时间模块
from django.utils import timezone
#导入系统自带用户模块
from django.contrib.auth.models import User

# Create your models here.
#新建BlogArticles，django中类表示表
class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    #author 被定义为外键，关联User表，related_name 表示允许通过类User 反向查询
    author = models.ForeignKey(User, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        #按照publish字段值倒序显示
        ordering = ("-publish",)
        #在admin页面显示表名称
        verbose_name_plural = 'BlogArticles'

    def __str__(self):
        return self.title


