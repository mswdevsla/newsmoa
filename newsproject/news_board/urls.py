from django.conf.urls import url
from newsproject.news_board import views

urlpatterns = [
    url(r'^notification', views.notification, name='news_notification'),
    url(r'^user_board', views.user_board, name='news_userboard')
]