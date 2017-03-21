from django.shortcuts import render
from newsproject.news_component.models import NewsContent

def config(request):
    contents = NewsContent.objects.all()
    sections = contents.values('news_section').distinct()
    print(NewsContent.CHOICES_SECTION[1][1])
    return render(request, 'news_component/config.html', context={
        'contents': contents,
        'sections': sections,
        'NewsContent': NewsContent
    })