#-*- coding: UTF-8 -*-

from django.shortcuts import render,render_to_response
from django.http import HttpResponse,HttpResponseRedirect
from django.template import RequestContext
from django import forms
from models import User


# Create your views here.
class UserForm(forms.Form): 
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())


def regist(req):
    if req.method == 'POST':
        #获得表单数据
        username = req.POST['username']
        password = req.POST['password']
        #添加到数据库
        user = User.objects.filter(username = username)
        if user:
            return HttpResponse("<div id='success'>username occupied, change it!</div>")
        User.objects.create(username= username,password=password)
        return HttpResponse("<div id='success'>regist success!!</div>")
    else:
        return HttpResponse("<div id='success'>regist failed!!</div>")


def regist_bak(req):
    if req.method == 'POST':
        uf = UserForm(req.POST)
        if uf.is_valid():
            #获得表单数据
            username = uf.cleaned_data['username']
            password = uf.cleaned_data['password']
            #添加到数据库
            User.objects.create(username= username,password=password)
            return HttpResponse("regist success!!<br><a href='/login'>back</a>")
    else:
        uf = UserForm()
    return render_to_response('login/regist.html',{'uf':uf}, context_instance=RequestContext(req))

def login(req):
    if req.method == 'POST':
        username = req.POST.get('username')
        password = req.POST.get('password')
        user = User.objects.filter(username__exact = username,password__exact = password)
        if user:
            response = HttpResponseRedirect('/todo')
            response.set_cookie('username',username,3600)#dead time is 60minutes
            return response
        else:
            return HttpResponseRedirect('/login/login/')
    return render_to_response('login/login.html',context_instance=RequestContext(req))

def index(req):
    username = req.COOKIES.get('username','')
    return render_to_response('login/index.html' ,{'username':username})

def logout(req):
    response = HttpResponseRedirect('/login/')
    #清理cookie里保存username
    response.delete_cookie('username')
    return response