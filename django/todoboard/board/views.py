# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse

from .models import User
from .models import Comment
from forms import commentform
# Create your views here.
def index(request):
    comment_list = Comment.objects.all()
    context = {"comment_list":comment_list}
    return render(request, 'index.html', context)

def postcomment(request, post_pk):
    postuser = get_object_or_404(User, pk=post_pk)
    if request.method == 'POST':
        form = commentform(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = postuser
            comment.save()
            comment_list = Comment.objects.all()
            context = {"comment_list":comment_list,
            "post_pk":post_pk
            }
            return render(request, 'postcomment.html',context)
        else:
            comment_list = Comment.objects.all()
            context = {"comment_list":comment_list,
            "post_pk":post_pk}
            return render(request, 'postcomment.html', context)
    else:
        comment_list = Comment.objects.all()
        context = {"comment_list":comment_list,
        "post_pk":post_pk}
        return render(request,'postcomment.html',context)
