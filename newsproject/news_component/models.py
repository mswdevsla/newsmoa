from django.db import models
# Create your models here.

class NewsCompany(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_company = models.CharField(max_length=16)
    xml_address = models.CharField(max_length=255)

class NewsSection(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_section = models.CharField(max_length=16)

class NewsComponent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_company = models.ForeignKey(NewsCompany)
    news_section = models.ForeignKey(NewsSection)