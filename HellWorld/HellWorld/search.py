from django.http import HttpResponse
from django.shortcuts import render
#表单
def search_form(request):
    return render(request, 'search_form.html')

# 接收请求数据
def search(request):
    request.encoding = 'utf-8'
    if 'q' in request.GET and request.GET['q']:
        if request.GET['q']=='北京':
            message = '恭喜你中奖了' + request.GET['q'] +'人！'
        else:
            message = '很遗憾你没中奖' + request.GET['q'] + '人！'
    else:
        message = '你提交了空表单'
    return HttpResponse(message)