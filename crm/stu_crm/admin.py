# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import stu_info
# Register your models here.

@admin.register(stu_info)
class stu_info(admin.ModelAdmin):
    list_display = ('id', 'QQ', 'name')
