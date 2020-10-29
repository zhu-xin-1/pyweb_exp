from django.shortcuts import render,HttpResponse
from app01 import models
from django.db.models import Avg,Max,Min,Count,Sum
# 以ORM的方法create 实现
def add_book(request):
    # #添加数据
    # books = models.Book.objects.create(title="黯然销魂掌", price=999,publish="金庸出版社",
    #                                pub_data="2020-10-10")
    # # 查找数据
    # books =models.Book.objects.all()
    # print(books,type(books))
    # #过滤数据 在过滤中使用模糊查询需要在名称后加__in 比如filter(price__in=[200,300])
    # books = models.Book.objects.filter(pk=5)
    # books = models.Book.objects.filter(publish='功夫出版社')
    # #查询不符合条件的数据
    #books=models.Book.objects.exclude(pk=5)#相当于不包含以上条件的数据
    # # get 用于查询符合的对象 并且只能有一个对象,多了则报错
    #books= models.Book.objects.get(pk=5)
    # # order_by() 对结果进行排序
    # books = models.Book.objects.order_by("price")#正序
    # books = models.Book.objects.order_by("-price")#反序
    # #reverse 反转
    #books = models.Book.objects.order_by("-price").reverse()#降序再反转
    # #count 计数
    # books = models.Book.object.count()#全部计数
    # books = models.Book.objects.filter(price=200).count()
    # first（）返回第一条数据
    # last() 返回最后一条
    # exists（） 查询数据是否存在 类型只能为QuerySet型
    # values() 查询部分字段
    # books = models.Book.objects.values("pk","price")
    # print(books[0]["price"],type(books))
    # values_list() 也是查询部分字段的数据 ，当只想要数据的时候使用
    # distinct() 对数据去重
    # 删除元素 使用数据类型.delete()
    # # books = models.Book.objects.filter(pk__in=[1, 2]).delete()#删除序号在1到2之间的数据
    #ORM添加数据
    # # 获取出版社对象
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # # 给书籍的出版社属性publish传出版社对象
    # book = models.Book.objects.create(title="菜鸟教程",price= 200,pub_data = "2010-10-10",publish=pub_obj)
    # # 常见使用id
    # pub_obj = models.Publish.objects.filter(pk=1).first()
    # #  获取出版社对象的id
    # pk = pub_obj.pk
    # #  给书籍的关联出版社字段 publish_id 传出版社对象的id
    # book = models.Book.objects.create(title="冲灵剑法", price=100, pub_date="2004-04-04", publish_id=pk)
    # print(book, type(book))
    # 传递对象形式
    # chong = models.Author.objects.filter(name="令狐冲").first()
    # ying = models.Author.objects.filter(name="任盈盈").first()
    # book = models.Book.objects.filter(title="菜鸟教程").first()
    # book.authors.add(chong,ying)
    # 聚合查询 aggregate 需要导入从db.models 中引入Avg,Max,Min,Count.Sum
    # res = models.Book.objects.aggregate(Avg("price"))
    # print(res,type(res))
    # 计算图书数量、最贵价格和最便宜价格
    # res = models.Book.objects.aggregate(c=Count("id"),max=Max("price"),min=Min("price"))
    # print(res)
    # 分组查询 annotate
    return HttpResponse("<p>添加成功！</p>")

# Create your views here.
