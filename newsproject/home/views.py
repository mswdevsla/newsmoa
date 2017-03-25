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
        news_contents = []
        news_customs = NewsCustom.objects.filter(user_info__user=request.user).order_by('priority')
        for news_custom in news_customs:
            i = 1
            feed = feedparser.parse(news_custom.news_content.xml_address)
            for item in feed.entries:
                item['news_company'] = news_custom.news_content.get_company_name
                news_contents.append(item)
                i = i+1
                if i > news_custom.how_many:
                    break

    return render(request, 'home.html', context=({
        'news_customs': news_customs,
        'news_contents': news_contents
    }))