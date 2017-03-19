from django.contrib.auth.models import User
from django.db import models
from newsproject.news_component.models import NewsCompany, NewsSection


# Create your models here.

class UserInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, null=True,  on_delete=models.SET_NULL, related_name='user_info')
    email = models.EmailField(null=True, db_index=True)
    is_admin_user = models.BooleanField(default=False)

class NewsCustom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_info = models.ForeignKey(UserInfo)
    news_company = models.ForeignKey(NewsCompany)
    news_section = models.ForeignKey(NewsSection)
    how_many = models.IntegerField(default=0)
    priority = models.IntegerField(default=99)