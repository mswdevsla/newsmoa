from django.shortcuts import render
from newsproject.news_component.models import NewsSection, NewsCompany, NewsComponent

def config(request):
    print(1)
    return render(request, 'news_component/config.html')