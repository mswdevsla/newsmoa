from django.conf.urls import url

from newsproject.home import views
from django.conf.urls import url, include

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^user/', include('newsproject.user.urls')),
]