import json

from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import user_table as User
import hashlib
# Create your views here.
def get_page(request):

    return render(request,'register/register.html')
def get_register(request):
    if request.method == 'GET':
        return render(request, 'register/register.html')
    if request.method == 'POST':
        if request.POST['user_name'] and request.POST['pwd']:
            name = request.POST.get('user_name')
            password = request.POST.get('pwd')
            m = hashlib.md5()
            m.update(password.encode())
            password = m.hexdigest()
            #检查用户名是否已经注册
            old_user = User.objects.filter(name = name)
            if old_user:
                return HttpResponse('用户名已注册')
            else:
                try:
                    User.objects.create(name=name,password=password)
                    return HttpResponse('注册成功')
                except Exception as e:
                    print('create username error %s'%(e))
                    return HttpResponse('用户名已注册')
        else:
            return HttpResponse('username or password is not allowed null')
    # return HttpResponse('ok')
def post_register_page(request):
    return render(request,'register/register_not_use_form.html')
def post_register_information(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        if not username:
            return HttpResponse('请输入用户名')
        print('username是',username)
        password = request.POST.get('password')
        if not password:
            return HttpResponse('请输入密码')
        m = hashlib.md5()
        m.update(password.encode())
        password = m.hexdigest()
        old_username = User.objects.filter(name=username)
        if old_username:
            return HttpResponse('the user is already registed')
        try:
            User.objects.create(name=username,password=password)
            return HttpResponse('注册成功')
        except Exception as e:
            return HttpResponse('注册发生错误，请稍后重试')

        return HttpResponse('your post is ok %s %s'%(username,password))
    else:
        return HttpResponse('the request method is not post ')


def checkusername(request):
    if request.method == 'GET':
        username = request.GET.get('username')
        username = User.objects.filter(name=username)
        if username:
            return HttpResponse('1')
        else:
            return HttpResponse('0')

def get_register_information(request):
    pass

def get_register_page(request):
    return render(request,'register/xhr_use_get.html')

def get_all_users(request):
    return render(request,'register/get_all_user.html')

def get_user_server(request):
    users = User.objects.all()#取数数据库中所有用户
    msg = ''
    for u in users:
        msg += '%s_%s|'%(u.name,u.password)
    # msg = msg.strip('|')
    last_msg = msg[0:-1]#字符串切片，切最后一个符号‘|’
    informations = json.dumps(last_msg)
    return HttpResponse(last_msg)

def json_dumps(request):
    #定义一个json对象
    dic = {
        "uname":"lili",
        "uage":30,
    }
    #定义一个json对象数组
    dic_arr = [
        { "uname":"lili",
        "uage":30,},
        { "uname":"rourou",
        "uage":31,}
    ]

    #当我们在dumps单个json对象成json字符串的时候，dumps出来的数据可能是无序的,所以指定sort_keys为True使dumps出来的字符串是有序的
    #因为在浏览器中显示的json字符串中间有间隔，所以使用separators方法指定键值对之间用冒号隔开，每个键值对之间用逗号隔开，这样就取消了json字符串中的空格，充分利用了网络资源
    json_str = json.dumps(dic,sort_keys=True,separators=(',',':'))
    json_str_arr = json.dumps(dic_arr)
    #如果是在数据库中拿的值，django还提供了一种更加方便的方法序列化json对象，同时达到取消序列化出的json字符串中有空格的情况
    from django.core import serializers
    json_users = User.objects.all()#这个查询方法返回的对象的类型是QuerySet
    print(type(json_users))
    json_str_all = serializers.serialize('json',json_users)#serialize方法的第一个参数指定的是序列化的格式是json字符串，第二个参数是接收QuerySet类型的参数，即数据库查询返回的数据类型
    return HttpResponse(json_str_all,content_type='application/json')#因为是HttpResponse返回数据，默认的content_type是text,为了严谨手动指定content_type


    """return JsonResponse({'uname':"xiaowang"}) 
    json对象有几种写法 [] {} [{}] {{}},这几种写法中JsonResponse不接受外面的括号是[]类型的json对象，这个需要注意
    serializers方法是django返回json字符串给前端的一种方法，下面是另一种方法,使用JsonResponse里面直接放json对象，json对象中的建可以不用双引号，返回给前端的时候会自动加上双引号
    使用这个方法返回json字符串不用再指定content_type='application/json'，因为JsonResponse明显是返回json字符串回前端
"""


def json_obj(request):

    return render(request,'register/json_obj.html')



