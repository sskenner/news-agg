# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article, Feed
# Create your views here.

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'news/articles_list.html', {'articles': articles})

def feeds_list(request):
		feeds = Feed.objects.all()
		return render(request, 'news/feeds_list.html', {'feeds': feeds})