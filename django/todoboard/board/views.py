# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .models import User
from .models import Comment
from forms import commentform
from forms import loginform
# Create your views here.
def index(request):
    comment_list = Comment.objects.all()
    context = {"comment_list":comment_list}
    return render(request, 'index.html', context)

def login(request):
    if request.method =='POST':
        form = loginform(request.POST)
        if form.is_valid():
            name = request.POST.get('username_text')
            pwd = request.POST.get('password')
            try:
                user_to_login = User.objects.get(username_text=name)

            except User.DoesNotExist:
                raise Http404("User does not exist")
                context = {"error":"User does not exist",}
                return render(request, 'board/login.html', context)

            if user_to_login.password == pwd:
                return HttpResponseRedirect(reverse('board:postcomment', args=(name,)))
            else:
                context = {"error":"Wrong password",}
                return render(request, 'board/login.html', context)
        else:
            context = {"error":"Not a valid form",}
            return render(request, 'board/login.html', context)
    else:
        context = {}
        return render(request,'board/login.html',context)



def postcomment(request, post_user):
    postuser = get_object_or_404(User, username_text=post_user)
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = postuser
            comment.save()
            comment_list = Comment.objects.all()
            #context = {"comment_list":comment_list,
            #"post_pk":post_pk
            #}
            return HttpResponseRedirect(reverse('board:postcomment', args=(post_user,)))
            #return render(request, 'postcomment.html',context)
        else:
            comment_list = Comment.objects.all()
            context = {"comment_list":comment_list,
            "post_user":post_user,
            "error":"This is not a valid form",}
            return render(request, 'board/postcomment.html', context)
    else:

        comment_list = Comment.objects.all()
        context = {"comment_list":comment_list,
        "post_user":post_user}
        return render(request,'board/postcomment.html',context)
