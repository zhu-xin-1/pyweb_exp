from django.urls import path,re_path
from app01 import views # 从自己的app中引入views
# urlpatterns = [
#     re_path(r'^login/(?P<m>[0-9]{2})/$' , views.index,),
# ]
urlpatterns = [
    path("add_book/", views.add_book),
]