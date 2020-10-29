from django.conf.urls import url
from django.urls import path
from . import views,testdb,search,search2
from django.conf.urls import url
# urlpatterns = [
#     # path('runoob/',views.runoob),
#     # path('testdb/',testdb.testdb),
#     #path(r'^keqiang$',views.keqiang),
#     url(r'^hello$', views.runoob),
#     url(r'^testdb$',testdb.testdb),
#     url(r'^search-form$', search.search_form),
#     url(r'^search$', search.search),
#     url(r'^search-post$',search2.search_post),
#
# ]
from django.contrib import admin
from django.urls import path,include
# 用于路由分发 解决所有url全在一个urls.py中造成的混乱,将url分发到各个APP中
urlpatterns =[
    path('admin/',admin.site.urls),

    #path("app01/", include("app01.urls")),
    #通过给路由器取别名 ，来反向解析出url
    path('runoob/',views.runoob),
    path('login1/', views.login, name="login"),
    path("app01/", include("app01.urls")),
    #path("app02/", include("app02.urls")),
]


# from django.urls import path
# urlpatterns=[
#     url(r"runoob/",views.runoob),
# ]