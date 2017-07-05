# -*- coding: utf-8 -*-

from django.http import HttpResponse
from django.shortcuts import render_to_response
from .models import User
from .models import Comment
from django import forms

class commentform(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']
