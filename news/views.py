# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Article, Feed
from .forms import FeedForm
from django.shortcuts import redirect

import feedparser
import datetime

# Create your views here.

def articles_list(request):
    articles = Article.objects.all()

    rows = [articles[x:x+1] for x in range(0, len(articles), 1)]

    return render(request, 'news/articles_list.html', {'rows': rows})

def feeds_list(request):
	feeds = Feed.objects.all()
	return render(request, 'news/feeds_list.html', {'feeds': feeds})

def new_feed(request):
	if request.method == "POST":
		form = FeedForm(request.POST)
		if form.is_valid():
			feed = form.save(commit=False)

			feedData = feedparser.parse(feed.url)


			# set some fields
			feed.title = feedData.feed.title
			feed.save()

			for entry in feedData.entries:
				article = Article()
				article.title = entry.title
				article.url = entry.link
				article.description = entry.description
				
				d = datetime.datetime(*(entry.published_parsed[0:6]))
				dateString = d.strftime('%Y-%m-%d %H:%M%:%S')

				article.publication_date = dateString
				article.feed = feed # why the parent-child relationship?
				article.save()

			return redirect('news.views.feeds_list') #not redirecting to feeds_list after save
	else:
		form = FeedForm()
	return render(request, 'news/new_feed.html', {'form': form})

# https://www.djangoproject.com/rss/weblog
#42:54