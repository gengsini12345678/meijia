from django.shortcuts import render,redirect
from django.urls import reverse

from django.contrib.auth.decorators import  login_required

from django.core.serializers import serialize
from django.http import HttpResponse
from . import models

import store

# Create your views here.

@login_required
def goods_upload(request,store_id):
    '''
    上传商品
    :param request:
    :param store_id:
    :return:
    '''

    if request.method == 'GET':
        goods_1_type = models.GoodsType.objects.filter(parent__isnull = True)
        return render(request,'goods/goods_upload.html',{'store_id':store_id,'goods_1_type':goods_1_type})

    elif request.method == 'POST':
        # 获取数据
        name = request.POST['name']
        price = request.POST['price']
        stock = request.POST['stock']
        intro = request.POST['intro']
        imgpath = request.FILES['imgpath']

        # 其他数据 ,获得二级类型的编号
        type_id = request.POST['type2']
        # print('---------------->',type_id)
        # 获取二级类型
        goodstype = models.GoodsType.objects.get(pk=type_id)
        # 所属店铺
        _store = store.models.Store.objects.get(pk=store_id)

        # 创建商品对象，完成上传操作
        goods = models.Goods(name=name,price=price,store=_store,goodstype=goodstype,
                             intro=intro,stock=stock,sale=0)
        goods.save()

        # 创建商品图片对象
        good_image = models.GoodsImage(path=imgpath,goods=goods)
        good_image.save()

        # 上传完成，跳转商品详情页面
        return redirect(reverse('goods:goods_info',kwargs={'goods_id':goods.id}))

def goods_info(request,goods_id):
    '''
    查看商品详情视图出来函数
    :param request:
    :return:
    '''
    # 查询到具体的商品
    goods = models.Goods.objects.get(pk=goods_id)
    return render(request,'goods/goods_info.html',{'goods':goods})




def goodstype(request):
    '''

    :param request:
    :return:
    '''
    # 获取类型编号并查询一级类型对象
    type_id = request.GET['ajax_type_id']
    goods_type = models.GoodsType.objects.get(pk=type_id)
    # 查询二级类型对象
    goods_type2_list = models.GoodsType.objects.filter(parent=goods_type)
    # 返回查询到的数据
    return HttpResponse(serialize('json',goods_type2_list))
