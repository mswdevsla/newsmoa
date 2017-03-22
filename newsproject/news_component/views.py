from django.shortcuts import render
from newsproject.news_component.models import NewsContent
from django.contrib.auth.decorators import login_required

# @login_required
def config(request):
    contents = NewsContent.objects.all()
    companys = contents.distinct('news_company')
    sections = contents.distinct('news_section')
    return render(request, 'news_component/config.html', context={
        'contents': contents,
        'companys': companys,
        'sections': sections,
        'NewsContent': NewsContent
    })