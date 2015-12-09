# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

def dbinsert(request):
    test1 = Test(name='sqy')
    test1.save()
    return HttpResponse("<p>数据插入成功</p>");