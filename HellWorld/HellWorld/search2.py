from django.shortcuts import render
from django.views.decorators import csrf

# 接收POST请求
def search_post(request):
    ctx={}
    if request.POST:
        ctx['rlt']= '您提交的内容为：'+ request.POST['q']
    return render(request,"post.html",ctx)