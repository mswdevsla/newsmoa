from django.conf.urls import url
from newsproject.news_board import views

urlpatterns = [
    url(r'^list$', views.board_list, name='board_list'),
    url(r'^write$', views.board_write, name='board_write'),
    url(r'^view/(?P<board_id>[0-9]+)$', views.board_view, name='board_view'),
    url(r'^modify/(?P<board_id>[0-9]+)$', views.board_modify, name='board_modify'),
]