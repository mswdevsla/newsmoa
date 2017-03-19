from django.conf.urls import url

from newsproject.user import views

urlpatterns = [
    url(r'^$', views.register, name='user_register'),
]