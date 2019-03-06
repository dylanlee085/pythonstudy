# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ArticleColumn
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@login_required(login_url='/account/login')
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)
    return render(request, "article/column/article_column.html", {"columns":columns})


@login_required(login_url='/account/login/')
@csrf_exempt
def article_column(request):
    if request.method == "GET":
        columns = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request, "article/column/article_column.html",{"columns":cloumns, 'column_form':column_form } )
    if request.method == "POST":
        column_name = request.POST['colum']
        columns = ArticleColumn.objects.filter(user_id=request.user.id, columns=column_name)
        if columns:
            return HttpResponse('2')
        else:
            ArticleColumn.objects.create(user=request.user, columns=column_name)
            return HttpResponse("1")


@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")













