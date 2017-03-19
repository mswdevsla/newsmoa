from django.conf.urls import url

from newsproject.news_component import views

urlpatterns = [
    url(r'^config', views.config, name='news_config'),
]