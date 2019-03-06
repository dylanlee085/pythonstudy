# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
#导入timezone模块
from django.utils import timezone
#导入django自带User模块
from django.contrib.auth.models import User

# Create your models here.

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User, related_name="blog_posts")
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ("-publish",)
#解决django admin页面管理项目名称多个s
        verbose_name_plural = 'BlogArticles'

    def __str__(self):
        return self.title