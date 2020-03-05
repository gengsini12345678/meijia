from django.conf.urls import url

from . import views

app_name = 'orders'

urlpatterns = [

    # 结算确认--展示用户要买的商品，同时检查是否有收获地址
    url(r'^order_confrim/$',views.order_confrim,name='order_confrim'),
    # 结算支付--展示支付的付款页面，进行金钱操作【模拟】
    url(r'^order_pay/$',views.order_pay,name='order_pay'),
    # 生成订单
    url(r'^order_done/$',views.order_done,name='order_done'),
    # 查询订单
    url(r'^order_list/$',views.order_list,name='order_list'),
    # 查询订单详情
    url(r'^(?P<order_id>\d+)/order_info/$',views.order_info,name='order_info'),

]