from django.db import models

# 导入django 框架内置的用户模块
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    '''
    定义了一个用户扩展数据类型
    要和系统内置的用户一对一关联
    '''

    # 定义扩展属性字段

    id = models.AutoField(primary_key=True)
    header = models.ImageField(upload_to='static/images/headers/',default='static/images/headers/default.jpg')
    nickname = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    gender = models.CharField(max_length=5)

    # 和系统内置用户关联
    user = models.OneToOneField(User,on_delete=models.CASCADE)


class Address(models.Model):
    '''
    用户收获地址
    '''
    id = models.AutoField(primary_key=True)
    recv = models.CharField(max_length=50,verbose_name='收货人')
    phone = models.CharField(max_length=20,verbose_name='电话')
    nation = models.CharField(max_length=50,verbose_name='国家')
    province = models.CharField(max_length=50,verbose_name='省区')
    city = models.CharField(max_length=50,verbose_name='市区')
    country = models.CharField(max_length=50,verbose_name='县区')
    street = models.CharField(max_length=50,verbose_name='街道')
    intro = models.CharField(max_length=50,verbose_name='详细地址')
    status = models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)




