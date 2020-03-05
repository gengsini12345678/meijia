from django.shortcuts import render
#require_GET  装饰器一般定义在视图函数上，指定视图函数的访问方式
from django.views.decorators.http import require_GET
# @login_required 定义在视图函数上  登录之后才能访问
from django.contrib.auth.decorators import login_required


import goods,store
# Create your views here.


@login_required
# @require_GET
def index(request):
    '''

    :param request:
    :return:
    '''
    # if request.method == 'GET':
    #     return render(request,'commen/index.html',{})

    goodstype_1_list = goods.models.GoodsType.objects.filter(parent__isnull=True)

    # 查询指定类型【8种类型】中指定的数据【切片】
    # （1）男装女装
    # goods_type_1 =  goods.models.GoodsType.objects.get(pk=1)
    # goods_type_1_list = goods.models.GoodsType.objects.filter(parent=goods_type_1)
    # goods_list_1 = goods.models.Goods.objects.filter(goodstype__in=goods_type_1_list)[:5]



    # ---
    # (1)男装女装
    goods_type_1 =  goods.models.GoodsType.objects.get(pk=1)
    # 根据男装女装来获取二级列表的所有内容
    goods_type_1_list = goods.models.GoodsType.objects.filter(parent=goods_type_1)
    goods_list_1 = goods.models.Goods.objects.filter(goodstype__in=goods_type_1_list)[:5]


    # (2)鞋包配件
    goods_type_2 =  goods.models.GoodsType.objects.get(pk=2)
    goods_type_2_list = goods.models.GoodsType.objects.filter(parent=goods_type_2)
    goods_list_2 = goods.models.Goods.objects.filter(goodstype__in=goods_type_2_list)[:5]

    # (3)家电数码
    goods_type_3 =  goods.models.GoodsType.objects.get(pk=3)
    goods_type_3_list = goods.models.GoodsType.objects.filter(parent=goods_type_3)
    goods_list_3 = goods.models.Goods.objects.filter(goodstype__in=goods_type_3_list)[:5]

    # (4)护肤美妆
    goods_type_4 =  goods.models.GoodsType.objects.get(pk=4)
    goods_type_4_list = goods.models.GoodsType.objects.filter(parent=goods_type_4)
    goods_list_4 = goods.models.Goods.objects.filter(goodstype__in=goods_type_4_list)[:5]

    # ---------------
    # (5)运动户外
    goods_type_5 =  goods.models.GoodsType.objects.get(pk=5)
    goods_type_5_list = goods.models.GoodsType.objects.filter(parent=goods_type_5)
    goods_list_5 = goods.models.Goods.objects.filter(goodstype__in=goods_type_5_list)[:5]

    # (6)美食生鲜
    goods_type_6 =  goods.models.GoodsType.objects.get(pk=6)
    goods_type_6_list = goods.models.GoodsType.objects.filter(parent=goods_type_6)
    goods_list_6 = goods.models.Goods.objects.filter(goodstype__in=goods_type_6_list)[:5]

    # (7)家居家饰
    goods_type_7 =  goods.models.GoodsType.objects.get(pk=7)
    goods_type_7_list = goods.models.GoodsType.objects.filter(parent=goods_type_7)
    goods_list_7 = goods.models.Goods.objects.filter(goodstype__in=goods_type_7_list)[:5]

    # (8)珠宝眼镜
    goods_type_8 =  goods.models.GoodsType.objects.get(pk=8)
    goods_type_8_list = goods.models.GoodsType.objects.filter(parent=goods_type_8)
    goods_list_8 = goods.models.Goods.objects.filter(goodstype__in=goods_type_8_list)[:5]

    #---
    # 热门店铺
    store_list = store.models.Store.objects.all()[:5]
    return render(request,'commen/index.html',{'goodstype_1_list':goodstype_1_list,
                                               'goods_list_1':goods_list_1,
                                               'goods_list_2':goods_list_2,
                                               'goods_list_3':goods_list_3,
                                               'goods_list_4':goods_list_4,
                                               'goods_list_5':goods_list_5,
                                               'goods_list_6':goods_list_6,
                                               'goods_list_7':goods_list_7,
                                               'goods_list_8':goods_list_8,
                                               'store_list':store_list})












# @require_GET
# def shopcart(request):
#     '''
#     测试函数
#     :param request:
#     :return:
#     '''
#
#     return render(request,'commen/shopcart.html',{})