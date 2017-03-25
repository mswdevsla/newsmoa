from django.shortcuts import render
from newsproject.news_component.models import NewsContent
from newsproject.user.models import NewsCustom
from django.contrib.auth.decorators import login_required

# @login_required
def config(request):
    from django.http import HttpResponse
    contents = NewsContent.objects.all()
    companys = contents.distinct('news_company')
    sections = contents.distinct('news_section')
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

                except:
                    NewsCustom.objects.create(user_info__user=request.user, news_content=news_content, how_many=how_many,
                                              priority=i)

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