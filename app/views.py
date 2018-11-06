import hashlib
import os
import uuid

from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from AXF import settings
from app.models import Wheel, Nav, Mustbuy, Shop, MainShow, Foodtypes, Goods, User, Cart


def home(request):

    wheels = Wheel.objects.all()

    navs = Nav.objects.all()

    mustbuys = Mustbuy.objects.all()

    shoplist = Shop.objects.all()
    shophead = shoplist[0]
    shoptab = shoplist[1:3]
    shopclass = shoplist[3:7]
    shopcommend = shoplist[7:11]



    mainshows = MainShow.objects.all()

    data = {
        'title':'首页',
        'wheels':wheels,
        'navs':navs,
        'mustbuys':mustbuys,
        'shophead':shophead,
        'shoptab':shoptab,
        'shopclass':shopclass,
        'shopcommend':shopcommend,
        'mainshows':mainshows,
    }

    return render(request, 'home/home.html', context=data)


def market(request,categoryid,childid,sortid):
    # 分类数据
    foodtypes = Foodtypes.objects.all()

    # 获取点击 历史
    typeIndex = int(request.COOKIES.get('typeIndex',0))
    # print(foodtypes[typeIndex])
    categoryid = foodtypes[typeIndex].typeid


    # 子类
    childtypenames = foodtypes.get(typeid=categoryid).childtypenames
    childlist = []
    for item in childtypenames.split('#'):
        arr = item.split(':')
        obj = {'childname':arr[0],'childid':arr[1]}
        childlist.append(obj)



    # 商品数据
    # goodslist = Goods.objects.all()

    # 根据商品分类 数据过滤
    if childid == '0':
        goodslist = Goods.objects.filter(categoryid=categoryid)
    else:
        goodslist = Goods.objects.filter(categoryid=categoryid,childcid=childid)


    # 排序处理
    if sortid == '1':
        goodslist = goodslist.order_by('productnum')
    if sortid == '2':
        goodslist = goodslist.order_by('price')
    if sortid == '3':
        goodslist = goodslist.order_by('-price')


    # 购物车数量问题
    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)
        carts = Cart.objects.filter(user=user).exclude(number=0)




    data = {
        'title':'闪购超市',
        'foodtypes':foodtypes,
        'goodslist':goodslist,
        'childlist':childlist,
        'categoryid':categoryid,
        'childid':childid,
        'cart':carts,

    }



    return render(request, 'market/market.html', context=data)


def cart(request):
    token = request.session.get('token')
    carts = []
    if token:
        user = User.objects.get(token=token)

        carts = Cart.objects.filter(user=user).exclude(number=0)


    response_data = {
        'title':'购物车',
        'carts':carts
    }
    return render(request, 'cart/cart.html',context=response_data)


def mine(request):
    token = request.session.get('token')

    responseData = {
        'title':'我的',
    }

    if token:
        user = User.objects.get(token=token)
        responseData['name'] = user.name
        responseData['rank'] = user.rank
        responseData['img'] = '/static/uploads/' + user.img

    else:
        responseData['name'] = '未登录'
        responseData['rank'] = '无等级（未登录）'
        responseData['img'] = '/static/uploads/axf.png'

    return render(request, 'mine/mine.html',context=responseData)


def registe(request):
    if request.method == 'POST':
        user = User()
        user.account = request.POST.get('account')
        user.password = generate_password(request.POST.get('password'))
        user.name = request.POST.get('name')
        user.tel = request.POST.get('tel')
        user.address = request.POST.get('address')

        imgName = user.account + '.png'
        imgPath = os.path.join(settings.MEDIA_ROOT,imgName)
        print(imgPath)
        file = request.FILES.get('file')
        with open(imgPath,'wb') as fp:
            for data in file.chunks():
                fp.write(data)
        user.img = imgName


        user.token = str(uuid.uuid5(uuid.uuid4(),'registe'))
        # 保存到数据库
        user.save()

        # 状态保持
        request.session['token'] = user.token

        # 重定向
        return redirect('axf:mine')

    elif request.method == 'GET':
        return render(request,'mine/registe.html')


def generate_password(password):
    sha = hashlib.sha512()
    sha.update(password.encode("utf-8"))
    return sha.hexdigest()


def quit(request):

    logout(request)
    return redirect('axf:mine')


def login(request):
    if request.method == 'POST':
        account = request.POST.get('account')
        password = request.POST.get('password')

        try:
            user = User.objects.get(account=account)
            if user.password != generate_password(password):
                return render(request,'mine/login.html',context={'error':'密码错误'})

            else:
                user.token = str(uuid.uuid5(uuid.uuid4(),'login'))
                user.save()
                # 状态保持
                request.session['token'] = user.token
                return redirect('axf:mine')


        except:

            return render(request,'mine/login.html',context={
                'error':'用户名有误，请检查后输入'
            })


    elif request.method == 'GET':
        return render(request,'mine/login.html')

# 用户验证
def checkuser(request):
    account = request.GET.get('account')
    try:
        user = User.objects.get(account=account)
        return JsonResponse({'msg':'用户名存在','status':'-1'})

    except:
        return JsonResponse({'msg':'用户名可用','status':'1'})

# 添加购物车
def addtocart(request):

    goodsid = request.GET.get('goodsid')

    token = request.session.get('token')

    response_data = {
        'msg':'',
        'status':'',
    }


    if token: # 有登录
        # print('yijingdenglu')

        user = User.objects.get(token=token)
        goods = Goods.objects.get(pk=goodsid)

        carts = Cart.objects.filter(goods=goods).filter(user=user)
        if carts.exists():
            cart = carts.first()
            cart.number = cart.number + 1
            if int(goods.storenums) < cart.number:
                cart.number = goods.storenums
            cart.save()

            response_data['msg'] = '添加购物车成功'
            response_data['status'] = 1
            response_data['number'] = cart.number
            return JsonResponse(response_data)
        else:
            cart = Cart()
            cart.user = user
            cart.goods = goods
            cart.number = 1
            cart.save()

            response_data['msg'] = '添加购物车成功'
            response_data['status'] = 1
            response_data['number'] = cart.number
            return JsonResponse(response_data)
    else:     # 未登录
        response_data['msg'] = '请登陆后操作'
        response_data['status'] = '-1'

        return JsonResponse(response_data)


def subtocart(request):
    token = request.session.get('token')
    user = User.objects.get(token=token)
    goodsid = request.GET.get('goodsid')
    goods = Goods.objects.get(pk=goodsid)


    carts = Cart.objects.filter(user=user).filter(goods=goods)
    cart = carts.first()
    cart.number = cart.number - 1
    cart.save()

    response_data = {
        'msg':'删减成功',
        'status':'1',
        'number':cart.number
    }
    return JsonResponse(response_data)


def changecartstatus(request):
    cartid = request.GET.get('cartid')
    cart = Cart.objects.get(pk=cartid)
    cart.isselect = not cart.isselect
    cart.save()

    response_data = {
        'msg':'修改状态成功',
        'status':'1',
        'isselect':cart.isselect
    }
    return JsonResponse(response_data)