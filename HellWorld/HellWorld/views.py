from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# def hello(request):
#     return HttpResponse("Hello world!")

def runoob(request):
    # context ={}
    # context['hello'] ='Hello World!'
    # return render(request,'runoob.html',context)
    # views_list = ["克强的网址","克强的第二网址","景强"]
    # views_dict= {}
    # import datetime
    # now = datetime.datetime.now()
    # view_str = "<a href='https://www.runoob.com/'>点击跳转</a>"
    # views_num = 99
    # views_list=[]#['abc','ab','a','abc']
    # output={"views_list":views_list,"num":views_num,"views_dict":views_dict,"now":now,"view_str":view_str}
    name="菜鸟教程"
    return render(request,"base.html", {"name":name})

def keqiang(request):
    name  ="克强教程"
    return render(request,"runoob.html", {"name":name})

# 用装饰器的方法实现post过权限
@csrf_exempt
def ke_post(request):
    name = request.POST.get("name")
    return HttpResponse(name)
#用于反向解析url
from django.urls import reverse
from django.shortcuts import redirect
def login(request):
    if request.method == "GET":
        return HttpResponse('克强')
    else:
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        if username=="菜鸟教程" and pwd=="菜鸟教程":
            return HttpResponse('菜鸟教程')
        else:
            return redirect(reverse('login'))