# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.shortcuts import render
from django.http import *
# Create your views here.
def index(request):
    return HttpResponse("oa")