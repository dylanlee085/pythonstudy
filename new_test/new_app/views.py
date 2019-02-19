# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators import csrf

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


# Create your views here.

#1.GET方法

#表单
def search_form(request):
    return render_to_response('search_form.html')


#接收请求数据
def search(request):
    request.encoding = 'utf-8'
    print request.GET
    if 'q' in request.GET:
        message = '你搜索的内容为：' + request.GET['q']
    else:
        message = '你提交了空表单'
    return HttpResponse(message)



#2.POST方法

# #接收post请求数据
def search_post(request):
    ctx = {'rlt': 10000}
    print request.POST
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)





