from django.contrib.auth.models import User
from django.db import models
from newsproject.news_component.models import NewsContent


# Create your models here.

class UserInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL, related_name='user_info')
    user_account = models.CharField(max_length=32)
    email = models.EmailField(null=True, db_index=True)
    is_admin_user = models.BooleanField(default=False)

class NewsCustom(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user_info = models.ForeignKey(UserInfo)
    news_content = models.ForeignKey(NewsContent)
    how_many = models.IntegerField(default=0)
    priority = models.IntegerField(default=99)