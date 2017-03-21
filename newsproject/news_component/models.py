from django.db import models
# Create your models here.

class NewsContent(models.Model):
    """
    뉴스 신문사들
    """
    NEWS_CHOSUN = 1
    NEWS_DONGA = 2
    NEWS_HANI = 3
    NEWS_JOINS = 4

    CHOICES_NEWS = (
        (NEWS_CHOSUN, '조선일보'),
        (NEWS_DONGA, '동아일보'),
        (NEWS_HANI, '한겨레'),
        (NEWS_JOINS, '중앙일보'),
    )

    CONTENT_NEWS_STR = {
        NEWS_CHOSUN: 'chosun',
        NEWS_DONGA: 'donga',
        NEWS_HANI: 'hani',
        NEWS_JOINS: 'joins'
    }

    """
    뉴스 섹션
    """
    SECTION_POLITICS = 1
    SECTION_ECONOMY = 2
    SECTION_SOCIETY = 3
    SECTION_INTENATIONAL = 4

    CHOICES_SECTION = (
        (SECTION_POLITICS, '정치'),
        (SECTION_ECONOMY, '경제'),
        (SECTION_SOCIETY, '사회'),
        (SECTION_INTENATIONAL, '국제'),
    )

    CONTENT_SECTION_STR = {
        SECTION_POLITICS: 'politics',
        SECTION_ECONOMY: 'economy',
        SECTION_SOCIETY: 'society',
        SECTION_INTENATIONAL: 'intenational'
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_company = models.IntegerField(choices=CHOICES_NEWS)
    xml_address = models.CharField(max_length=255)
    news_section = models.IntegerField(choices=CHOICES_SECTION)
