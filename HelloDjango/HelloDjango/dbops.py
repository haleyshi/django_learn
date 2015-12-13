# -*- coding: utf-8 -*-

from django.http import HttpResponse
from TestModel.models import Test

def dbquery(request):
    list = Test.objects.all()
    list2 = Test.objects.filter(id=2)
    res3 = Test.objects.get(id=1)
    list4 = Test.objects.all().order_by('name')[0:2]
    list5 = Test.objects.all().order_by('name')

    response = "<p>All: "

    for var in list:
        response += var.name + " "

    response += "</p>"

    response += "<p>id=2: "

    for var in list2:
        response += var.name + " "

    response += "</p>"

    response += "<p>id=1: " + res3.name + "</p>"

    response += "<p>All order by name [0:2]: "

    for var in list4:
        response += var.name + " "

    response += "</p>"

    response += "<p>All order by name: "

    for var in list5:
        response += var.name + " "

    response += "</p>"

    return HttpResponse(response)


def dbinsert(request):
    test1 = Test(name='sqy')
    test1.save()
    return HttpResponse("<p>插入成功!<a href='../dbquery'>查询</a></p>");


def dbupdate(request):
    test1 = Test.objects.get(id=1)
    test1.name = "SQY"
    test1.save()

    Test.objects.filter(id=2).update(name="SGH")

    #Test.objects.all().update(name="WQ")

    return HttpResponse("<p>修改成功!<a href='../dbquery'>查询</a></p>")


def dbdelete(request):
    test1 = Test.objects.get(id=3)

    test1.delete()

    #Test.objects.filter(id=3).delete()
    #Test.objects.all.delete()

    return HttpResponse("<p>删除成功!<a href='../dbquery'>查询</a></p>")