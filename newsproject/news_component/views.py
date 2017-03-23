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

def sections(request):
    sections = NewsContent.objects.all().distinct('news_section')
    section_list = []
    for section in sections:

        section_list.append(section.get_section_name)

    print(section_list)
    return render(request, 'news_component/section_list.html')