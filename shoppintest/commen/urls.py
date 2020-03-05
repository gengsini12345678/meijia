from django.conf.urls import url

from . import views

app_name = 'commen'

urlpatterns = [
     # url(r'^shopcart/',views.shopcart,name='shopcart'),
    url(r'^.*$',views.index,name='index'),


]