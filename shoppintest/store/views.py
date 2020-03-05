from django.shortcuts import render,redirect
from  django.urls import reverse


from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_GET

from . import models

# Create your views here.
@login_required
def store_add(request):
    '''
    开店视图出图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request,'store/store_add.html',{})

    elif request.method == 'POST':
        # 获取数据
        name = request.POST['name']

        intro = request.POST['intro']

        user = request.user
        print("------------",user)

        try:
            cover = request.FILES['cover']
            store = models.Store(name=name,cover=cover,user=user,intro=intro)
        except:
            store = models.Store(name=name,user=user,intro=intro)

        store.save()
        return render(request,'store/store_add.html',{'error_code':0,'error_msg':'开店成功'})

@login_required
@require_GET
def store_list(request):

    '''
    查看所有店铺视图处理函数
    :param request:
    :return:
    '''
    # if request.method == 'GET':
    #     return render(request,'store/store_list.html',{})

    store_list = models.Store.objects.filter(user=request.user,status__in = [0,1])
    return render(request,'store/store_list.html',{'store_list':store_list})

@login_required
@require_GET
def store_info(request,store_id):
    '''
    店铺详情视图处理函数
    :param request:
    :return:
    '''
    # if request.method == 'GET':
    #     return render(request,'store/store_info.html',{})

    store = models.Store.objects.get(pk=store_id)
    return render(request,'store/store_info.html',{'store':store})





@login_required
def store_update(request, store_id):
    '''
    修改店铺视图处理函数
    :param request:
    :return:
    '''
    store = models.Store.objects.get(pk=store_id)
    if request.method == 'GET':

        return render(request,'store/store_update.html',{'store':store})

    elif request.method == 'POST':

        # 获取数据
        name = request.POST['name']
        intro = request.POST['intro']
        status = request.POST['status']

        try:
            cover = request.FILES['cover']
            store.cover = cover
        except:
            pass

        store.name = name
        store.intro = intro
        store.status = status
        store.save()
        # 重定向到 店铺详情store_info页面
        return redirect(reverse('store:store_info',kwargs={'store_id':store.id}))




@login_required
@require_GET
def store_close(request,store_id):
    '''
    关闭店铺
    :param request:
    :return:
    '''
    # 查看店铺
    store = models.Store.objects.get(pk = store_id)
    store.status = 1
    store.save()
    return redirect(reverse('store:store_info',kwargs={'store_id':store.id}))



@login_required
@require_GET
def store_delete(request,store_id):
    '''
    删除店铺
    :param request:
    :return:
    '''
     # 查看店铺
    store = models.Store.objects.get(pk=store_id)
    store.status = 2
    store.save()
    return redirect(reverse('store:store_list'))


