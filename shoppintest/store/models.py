from django.db import models

from django.contrib.auth.models import User

# Create your models here.

class Store(models.Model):
    '''
    店铺数据模型
    '''
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    cover = models.ImageField(upload_to='static/images/store/',default='static/images/store/store.jpg')

    # 0 正常 1 关闭 2.删除  其他--永久删除
    status = models.IntegerField(default=0)
    intro = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
