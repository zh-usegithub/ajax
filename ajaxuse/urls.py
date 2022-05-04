from django.urls import path, include
from . import views
#此代码示例路由/start/make_get使用了get及post的xhr请求方式，可以参照其实现方式进行复习
urlpatterns = [
    path('register/',views.get_register),
    path('register_page/',views.get_page),
    path('make_post/',views.post_register_page),
    path('make_post/information',views.post_register_information),
    path('make_get/',views.get_register_page),#用户注册界面
    path('make_get/information',views.get_register_information),
    path('make_get/checkusername',views.checkusername),
    path('user/get_all_user_page',views.get_all_users),#获取所有用户界面
    path('user/get_all_user_information',views.get_user_server),
    path('json_obj/',views.json_obj),
    path('json_dumps/',views.json_dumps)
]
