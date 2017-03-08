from django.shortcuts import render
import feedparser
# Create your views here.

def home(request):
    feed = feedparser.parse('http://myhome.chosun.com/rss/www_section_rss.xml')
    feed = feed.entries
    for item in feed:
        print(item)
    return render(request, 'home.html', context=({
        'feed': feed
    }))