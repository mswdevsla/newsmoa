from django.conf.urls import url
from newsproject.news_board import views

urlpatterns = [
    url(r'^notification$', views.notification, name='news_notification'),
    url(r'^user_board$', views.user_board, name='news_userboard'),
    url(r'^bitcoin', views.bitcoin, name='news_bitcoin'),
    url(r'^write$', views.board_write, name='board_write'),
    url(r'^view/(?P<board_id>[0-9]+)$', views.board_view, name='board_view'),
]