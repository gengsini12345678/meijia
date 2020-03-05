from django.shortcuts import render,redirect
from django.urls import reverse

import shopcart,users


from . import models

# Create your views here.
def order_confrim(request):
    '''
    订单确认页面
    :param request:
    :return:
    '''
    shopcart_id_list = request.POST.getlist('buy_goods_id')
    shopcart_list = shopcart.models.Shopcart.objects.filter(pk__in = shopcart_id_list)
    # print(buy_goods_list)

    return render(request,'orders/order_confirm.html',{'shopcart_list':shopcart_list})


def order_pay(request):
    '''
    结算支付
    :param request:
    :return:
    '''
    pass

def order_done(request):
    '''
    结算支付
    :param request:
    :return:
    '''
    # 获取购买的商品
    shopcart_list = request.POST.getlist('sc')

    # 获取收货地址
    addr_id = request.POST['addr_id']
    # print("---------------------",addr_id)
    address = users.models.Address.objects.get(pk=addr_id)
    addr = address.recv+";"+address.phone+";"+address.nation+";"+address.province+";"\
           +address.city+";"+address.country+";"+address.street+";"+address.intro

    total = 0

    # 生成订单

    myorder = models.MyOrder(user_id = request.user.id,address=addr,total=total)
    myorder.save()
    # 创建订单项对象
    for sc_id in shopcart_list:
        # 查询购物车对象
        _shopcart = shopcart.models.Shopcart.objects.get(pk=sc_id)
        # 创建订单项对象
        order_item = models.MyOrderItem(goods_img = _shopcart.goods.goodsimage_set.first().path,
                                        goods_name = _shopcart.goods.name,goods_price= _shopcart.goods.price,
                                        goods_count =_shopcart.count,goods_subtotal= _shopcart.subtotal,
                                        myorder=myorder)
        order_item.save()
        total += _shopcart.subtotal

    myorder.total = total
    myorder.save()



    # 保存订单跳转到订单详情界面

    return redirect(reverse('orders:order_info',kwargs={"order_id":myorder.id}))



def order_list(request):
    '''
    结算支付
    :param request:
    :return:
    '''
    _order_list = models.MyOrder.objects.filter(user_id = request.user.id)
    return render(request,'orders/order_list.html',{'order_list':_order_list})

def order_info(request,order_id):
    '''
    查看单个订单详情
    :param request:
    :return:
    '''
    _order = models.MyOrder.objects.get(pk=order_id)
    return render(request,'orders/order_info.html',{"order":_order})