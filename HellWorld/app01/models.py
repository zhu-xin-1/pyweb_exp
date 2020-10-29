from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True) #id自动创建
    title = models.CharField(max_length=32) #书籍名称
    price = models.DecimalField(max_digits=5, decimal_places=2)
    publish = models.CharField(max_length=32)#出版社名称
    pub_data = models.DateField() #出版时间