from django.http import HttpResponse
from django.shortcuts import render
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
    return render(request,"runoob.html", {"name":name})

