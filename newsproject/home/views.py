from django.shortcuts import render
import feedparser
# Create your views here.

def home(request):
    feed = feedparser.parse('http://myhome.chosun.com/rss/www_section_rss.xml')
    feed = feed.entries
    i = 0
    content = []
    for item in feed:
        content.append(item)
        print(content)
        if i > 2:
            break
        i = i+1
    return render(request, 'home.html', context=({
        'content': content
    }))