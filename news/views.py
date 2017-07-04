# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect

# Create your views here.

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'news/articles_list.html', {'articles': articles})

def feeds_list(request):
	feeds = Feed.objects.all()
	return render(request, 'news/feeds_list.html', {'feeds': feeds})

def new_feed(request):
	if request.method == "POST":
		form = FeedForm(request.POST)
		if form.is_valid():
			feed = form.save(commit=False)
			# set some fields
			feed.title = "title"
			feed.save()
			return redirect('news.views.feeds_list') #not redirecting to feeds_list after save
	else:
		form = FeedForm()
	return render(request, 'news/new_feed.html', {'form': form})

# https://www.djangoproject.com/rss/weblog