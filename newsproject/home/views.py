from django.shortcuts import render
import feedparser
from newsproject.user.models import NewsCustom
from html.parser import HTMLParser
# Create your views here.


def home(request):
    news_contents = []
    if request.user.is_authenticated:
        news_customs = NewsCustom.objects.filter(user_info__user=request.user).order_by('priority')
        for news_custom in news_customs:
            i = 1
            feed = feedparser.parse(news_custom.news_content.xml_address)
            for item in feed.entries:
                item['news_company'] = news_custom.news_content.get_company_name
                item['news_section'] = news_custom.news_content.get_section_name
                parser = MyHTMLParser()
                parser.feed(item.summary)
                item['img'] = parser.imgtag
                parser.close()
                news_contents.append(item)
                i = i+1
                if i > news_custom.how_many:
                    break
    else:
        feed = feedparser.parse('http://rss.joins.com/joins_news_list.xml')
        feed = feed.entries
        i = 0
        for item in feed:
            news_contents.append(item)
            if i > 2:
                break
            i = i + 1
        news_customs = None

    return render(request, 'home.html', context=({
        'news_customs': news_customs,
        'news_contents': news_contents
    }))

class MyHTMLParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.reset()
        self.imgtag = ''

    def handle_starttag(self, tag, attrs):
        if tag.lower() == 'img':
            for attr in attrs:
                if attr[0] == 'src':
                    self.imgtag = attr[1]
