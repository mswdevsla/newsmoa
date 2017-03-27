from django.conf.urls import url

from newsproject.news_component import views

urlpatterns = [
    url(r'^config', views.config, name='news_config'),
    url(r'^section/list', views.section_list, name='section_list'),
    url(r'^section/home', views.section_home, name='section_home'),
    url(r'^company/list', views.company_list, name='company_list'),
    url(r'^company/home', views.company_home, name='company_home'),
]