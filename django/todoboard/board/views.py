# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .models import User
from .models import Comment
from .models import Todo
from forms import commentform
from forms import loginform
from forms import registerform,todoform
import json
from django.views.decorators.csrf import csrf_exempt



# Create your views here.

def register(request):
    if request.method =='POST':
        form = registerform(request.POST)
        if form.is_valid():
            name = request.POST.get('username_text')
            try:
                user_to_login = User.objects.get(username_text=name)
                context = {"error":"Username exists",}
                return render(request, 'board/register.html', context)
            except User.DoesNotExist:
                usr = form.save(commit=False)
                usr.save()
                request.session['logged_in_users'] = usr.username_text
                return HttpResponseRedirect(reverse('board:userpage', args=(usr.username_text,)))
        else:
            context = {"error":"Not a valid form",}
            return render(request, 'board/register.html', context)
    else:
        context = {}
        return render(request,'board/register.html',context)


def login(request):
    if request.method =='POST':
        form = loginform(request.POST)
        if form.is_valid():
            name = request.POST.get('username_text')
            pwd = request.POST.get('password')
            try:
                user_to_login = User.objects.get(username_text=name)

            except User.DoesNotExist:

                context = {"error":"User does not exist",}
                return render(request, 'board/login.html', context)

            if user_to_login.password == pwd:
                request.session['logged_in_user'] = name
                return HttpResponseRedirect(reverse('board:userpage', args=(name,)))
            else:
                context = {"error":"Wrong password",}
                return render(request, 'board/login.html', context)
        else:
            context = {"error":"Not a valid form",}
            return render(request, 'board/login.html', context)
    else:
        context = {}
        return render(request,'board/login.html',context)

def logout(request):
    try:
        del request.session['logged_in_user']
    except KeyError:
        pass
    return HttpResponseRedirect(reverse('board:login'))


def userpage(request, post_user):
    postuser = get_object_or_404(User, username_text=post_user)
    if post_user == request.session.get('logged_in_user'):
        if request.method == 'POST':
            form = commentform(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = postuser
                comment.save()

                return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))
            else:
                comment_list = Comment.objects.all()
                todo_list = Todo.objects.all()
                context = {"comment_list":comment_list,
                "todo_list":todo_list,
                "post_user":post_user,
                "error":"This is not a valid form",}
                return render(request, 'board/userpage.html', context)
        else:
            todo_list = Todo.objects.all()
            comment_list = Comment.objects.all()
            context = {"comment_list":comment_list,
            "todo_list":todo_list,
            "post_user":post_user}
            return render(request,'board/userpage.html',context)
    else:
        return HttpResponseRedirect(reverse('board:login'))



def add_todo(request,post_user):
    postuser = get_object_or_404(User, username_text=post_user)
    if post_user == request.session.get('logged_in_user'):
        if request.method == 'POST':
            form = todoform(request.POST)
            if form.is_valid():
                todo = form.save(commit=False)
                todo.user = postuser
                todo.save()
                return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))
            else:
                todo_list = Todo.objects.all()
                comment_list = Comment.objects.all()
                context = {"comment_list":comment_list,
                "todo_list":todo_list,
                "post_user":post_user,
                "error":"This is not a valid form",}
                return render(request, 'board/userpage.html', context)
        else:
            return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))
    else:
        return HttpResponseRedirect(reverse('board:login'))

def delete_comment(request,post_user):
    postuser = get_object_or_404(User, username_text=post_user)
    if post_user == request.session.get('logged_in_user'):
        if request.method == 'POST':
            id_num=request.POST['delete']
            comment = Comment.objects.filter(comment_id=id_num)
            comment.delete()
            return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))
        else:
            return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))

    else:
        return HttpResponseRedirect(reverse('board:login'))

def delete_todo(request,post_user):
    postuser = get_object_or_404(User, username_text=post_user)
    if post_user == request.session.get('logged_in_user'):
        if request.method == 'POST':
            id_num=request.POST['delete']
            todo = Todo.objects.filter(todo_id=id_num)
            todo.delete()
            return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))
        else:
            return HttpResponseRedirect(reverse('board:userpage', args=(post_user,)))

    else:
        return HttpResponseRedirect(reverse('board:login'))
