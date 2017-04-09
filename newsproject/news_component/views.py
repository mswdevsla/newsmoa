from django.shortcuts import render
from newsproject.news_component.models import NewsContent
from newsproject.user.models import NewsCustom
import feedparser
from html.parser import HTMLParser
from django.contrib.auth.decorators import login_required


@login_required
def config(request):
    from django.http import HttpResponse
    contents = NewsContent.objects.all()
    companys = contents.distinct('news_company')
    sections = contents.distinct('news_section')

    my_news = NewsCustom.objects.filter(user_info__user=request.user).order_by('priority')
    my_news_count = my_news.count()
    loop_times = {}
    loop_times['loop_times'] = range(1, 11)

    if request.method == 'POST':
        for i in range(1, 11):
            if not request.POST.get('section' + str(i)) == None and not request.POST.get('company' + str(i)) == None and not request.POST.get('how_many' + str(i)) == None:
                news_section = request.POST.get('section' + str(i))
                news_company = request.POST.get('company' + str(i))
                how_many = request.POST.get('how_many' + str(i))
                try:
                    news_content = NewsContent.objects.get(news_section=news_section, news_company=news_company)
                except:
                    return HttpResponse('<script>alert("해당하는 신문사의 섹션이 존재하지 않습니다"); history.back();</script>')

                try:
                    news_custom = NewsCustom.objects.get(user_info__user=request.user, priority=i)
                    news_custom.news_section = news_section
                    news_custom.news_company = news_company
                    news_custom.how_many = how_many
                    news_custom.save()
                except NewsCustom.DoesNotExist:
                    NewsCustom.objects.create(user_info=request.user.user_info, news_content=news_content, how_many=how_many, priority=i)
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect('/news_component/config')

    return render(request, 'news_component/config.html', context={
        'contents': contents,
        'companys': companys,
        'sections': sections,
        'NewsContent': NewsContent,
        'my_news': my_news,
        'my_news_count': my_news_count,
        'loop_times': loop_times['loop_times']
    })


def section_list(request):
    section = request.GET.get('section')

    if not section == None:
        contents = NewsContent.objects.filter(news_section=section)
    else:
        contents = NewsContent.objects.all().distinct('news_section')
    contents_list = []
    default_num = 1
    default_maxnum = 5
    for content in contents:
        i = 0
        feed = feedparser.parse(content.xml_address)
        for item in feed.entries:
            if i > 0:
                break
            item['news_company'] = content.get_company_name
            item['news_section'] = content.get_section_name
            item['news_image'] = 'newsproject/image/news_company' + str(content.news_company) + '.png'
            parser = MyHTMLParser()
            if hasattr(item, 'summary'):
                parser.feed(item.summary)
                item['img'] = parser.imgtag
            parser.close()
            contents_list.append(item)
            i = i + 1

        default_num = default_num + 1
        if default_num > default_maxnum:
            break
    return render(request, 'news_component/section_list.html', context={
        'contents_list': contents_list
    })


def section_home(request):
    section_contents = NewsContent.objects.all().distinct('news_section')

    return render(request, 'news_component/section_home.html', context={
        'section_contents': section_contents
    })


def company_list(request):
    company = request.GET.get('company')

    if not company == None:
        contents = NewsContent.objects.filter(news_company=company)
    else:
        contents = NewsContent.objects.all().distinct('news_company')
    contents_list = []
    default_num = 1
    default_maxnum = 5
    for content in contents:
        i = 0
        feed = feedparser.parse(content.xml_address)
        for item in feed.entries:
            if i > 0:
                break
            item['news_company'] = content.get_company_name
            item['news_section'] = content.get_section_name
            item['news_image'] = 'newsproject/image/news_company' + str(content.news_company) + '.png'
            parser = MyHTMLParser()
            if hasattr(item, 'summary'):
                parser.feed(item.summary)
                item['img'] = parser.imgtag
            parser.close()
            contents_list.append(item)
            i = i + 1

        default_num = default_num + 1
        if default_num > default_maxnum:
            break
    return render(request, 'news_component/company_list.html', context={
        'contents_list': contents_list
    })


def company_home(request):
    company_contents = NewsContent.objects.all().distinct('news_company')

    return render(request, 'news_component/company_home.html', context={
        'company_contents': company_contents
    })


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
