# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserInfo

# Register your models here.

# class UserProfielAdmin(admin.ModelAdmin):
#     list_display = ('user', 'phone')
#     # list_filter = ("phone",)

# admin.site.register(UserProfile, UserProfielAdmin)


class UserInfoAdmin(admin.ModelAdmin):
    list_display = ("user", "school", "company", "profession", "address", "aboutme", "photo")
    list_filter = ("school", "company", "profession")

admin.site.register(UserInfo, UserInfoAdmin)