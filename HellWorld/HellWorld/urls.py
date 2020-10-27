from django.conf.urls import url
from django.urls import path
from . import views,testdb

urlpatterns = [
    path('runoob/',views.runoob),
    path('testdb/',testdb.testdb)
]
# from django.urls import path
# urlpatterns=[
#     url(r"runoob/",views.runoob),
# ]