# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import User
from .models import Comment
from django import forms
from .models import Todo

class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']

class loginform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username_text','password']

class registerform(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username_text','password']

class todoform(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['todo_text','note']
