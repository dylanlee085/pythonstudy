# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'stu_crm/dashboard.html')

def customer(request):
    customers = models.Customer.objects.all()
    return render(request, 'stu_crm/customers.html', {'customers_list':customers})
