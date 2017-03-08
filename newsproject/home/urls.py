from django.conf.urls import url

from newsproject.home import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
]