from django.shortcuts import render
import feedparser
from newsproject.user.models import NewsCustom
# Create your views here.

def home(request):
    feed = feedparser.parse('http://rss.joins.com/joins_news_list.xml')
    feed = feed.entries
    i = 0
    content = []
    for item in feed:
        content.append(item)
        print(content)
        if i > 2:
            break
        i = i+1

    if request.user.is_authenticated:
        news_customs = NewsCustom.objects.filter(user_info__user=request.user)
    else:
        news_customs = None

    return render(request, 'home.html', context=({
        'content': content,
        'news_customs': news_customs
    }))