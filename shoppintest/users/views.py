from django.shortcuts import render,redirect
from django.urls import reverse


from  django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout



from . import models
# Create your views here.


def user_register(request):
    '''
    用户注册
    :param request:
    :return:
    '''

    if request.method == 'GET':
        return render(request,'users/register.html',{})

    elif request.method == 'POST':
        # 获取用户数据
        username = request.POST['username']
        userpass = request.POST['userpass']
        re_userpass = request.POST['re_userpass']
        nickname = request.POST['nickname']

        # 判断账号是否可用
        try:
            user = User.objects.get(username=username)
            return render(request,'users/register.html',{'error_code':-1,'error_msg':'账号已经存在'})


        except:
            # 判断昵称是否可用
            try:
                user_profile = User.userprofile.objects.get(nickname=nickname)
                return render(request,'users/register.html',{'error_code':-2,'error_msg':'昵称已经存在'})

            except:
                # 两次密码是否一致
                if userpass != re_userpass:
                    return render(request,'users/register.html',{'error_code':-3,'error_msg':'两次的密码不一致'})

                # 创建用户注册
                user = User.objects.create_user(username=username,password=userpass)

                # 创建扩展用户资料
                userprofile = models.UserProfile(nickname=nickname,phone='待完善',gender='待完善',user=user)
                # 保存数据
                user.save()
                userprofile.save()
                return render(request,'users/login.html',{'error_code':1,'error_msg':'注册成功，请使用新账号登录'})


def user_login(request):
    '''
    登录视图处理函数
    :param request:
    :return:
    '''

    if request.method == 'GET':

        # 登录成功字后要跳转的下一个路径
        try:
            next_url = request.GET['next']
        except:
            next_url = "/"
        return render(request,'users/login.html',{"next_url":next_url})


        return render(request,'users/login.html',{})

    elif request.method == 'POST':
        # 获取数据

        username = request.POST['username']
        userpass = request.POST['userpass']
        #  跳转的下一个网页路径
        next_url = request.POST['next_url']

        # 判断验证登录
        user = authenticate(username=username,password = userpass)

        if user is not None:
            # 验证账号是否锁定
            if user.is_active:
                # 记录登录状态，跳转页面
                login(request,user)
                # return render(request,'users/login.html',{'error_code':0,"error_msg":"登录成功"})
                # return redirect(reverse('commen:index'))
                if next_url is None:
                    next_url = '/'
                return redirect(next_url)


            else:
                return render(request,'users/login.html',{'error_code':-2,"error_msg":"账号被锁定"})

        else:
            return render(request,'users/login.html',{'error_code':-1,"error_msg":"账号或密码有误"})

def user_logout(request):
    '''
    退出视图处理函数
    :param request:
    :return:
    '''
    logout(request)
    return render(request,'users/login.html',{'error_code':0,"error_msg":"系统已退出"})


def address_add(request):
    '''
    添加地址视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        return render(request,'users/address_add.html',{})

    elif request.method == 'POST':
        # 获取数据，
        recv = request.POST['recv']
        phone = request.POST['phone']
        nation = request.POST['nation']
        province = request.POST['province']
        city = request.POST['city']
        country = request.POST['country']
        street = request.POST['street']
        intro = request.POST['intro']

        try:
            set_default = request.POST['set_default']
            # 修改原有地址为非默认地址
            address_list = models.Address.objects.filter(user_id = request.user.id)
            for addr in address_list:
                addr.status = False
                addr.save()

            # 如果当前地址为默认地址
            address = models.Address(nation=nation,province=province,phone=phone,
                                     country=country,city=city,intro=intro,user_id = request.user.id,
                                     recv=recv,street=street,status=True)
        except:
            address = models.Address(nation=nation,province=province,phone=phone,
                                     country=country,city=city,intro=intro,user_id = request.user.id,
                                     recv=recv,street=street,status=False)

        address.save()

        return redirect(reverse('users:address_list'))



def address_list(request):
    '''
    查看所有地址视图处理函数
    :param request:
    :return:
    '''
    if request.method == 'GET':
        _address_list = models.Address.objects.filter(user_id = request.user.id)
        return render(request,'users/address_list.html',{'address_list':_address_list})












