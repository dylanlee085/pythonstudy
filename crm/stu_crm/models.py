# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class stu_info(models.Model):
    QQ = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    channel = models.CharField(max_length=100)
    classes = models.CharField(max_length=100)
    class_type = models.CharField(max_length=100)
    details = models.CharField(max_length=200)
    status = models.BooleanField(default=False)
