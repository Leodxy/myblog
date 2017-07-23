from django.shortcuts import render,redirect
from .forms import RegisterForm
from . import models
import hashlib
from django.contrib.auth import get_user_model
User = get_user_model()
# 加密
def md5(password):
    md=hashlib.md5()
    md.update(password.encode())
    return md.hexdigest()
# Create your views here.
def register(request):
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)
        # 验证数据的合法性
        if form.is_valid():
            # password = md5(request.POST.get("password"))
            # data=form.cleaned_data()
            # models.User.objects.create(**data,password=password)
            form.save()
            return redirect('/user/login')
    else:
            # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()
            # 渲染模板
            # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
            # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'user/register.html', context={'form': form})

def index(request):
    return redirect('/index')