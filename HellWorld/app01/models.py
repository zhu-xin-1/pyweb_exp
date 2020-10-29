from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=32) #书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)
    # 用于设置外键 FroeignKey
    publish = models.ForeignKey("Publish", on_delete=models.CASCADE)#出版社名称
    pub_date = models.DateField() #出版时间
    #多对多键
    authors = models.ManyToManyField("Author")

# Create your models here.
class Publish(models.Model):
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=64)
    email = models.EmailField()

class Author(models.Model):
    name = models.CharField(max_length=32)
    age = models.SmallIntegerField()
    #一对一键
    au_detail = models.OneToOneField("AuthorDetail", on_delete=models.CASCADE)

class AuthorDetail(models.Model):
    gender_choices = (
        (0, "女"),
        (1, "男"),
        (2, "保密"),
    )
    gender = models.SmallIntegerField(choices=gender_choices)
    tel = models.CharField(max_length=32)
    addr = models.CharField(max_length=64)
    birthday = models.DateField()