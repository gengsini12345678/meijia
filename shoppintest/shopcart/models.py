from django.db import models
from django.contrib.auth.models import User


import goods

# Create your models here.

class Shopcart(models.Model):

    '''
    购物车数据模型
    '''
    id = models.AutoField(primary_key=True)
    goods = models.ForeignKey(goods.models.Goods,on_delete=models.CASCADE)
    # 商品数量
    count = models.IntegerField(default=1)
    #
    subtotal = models.FloatField()
    # 所属用户
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    add_time = models.DateTimeField(auto_now_add=True)






