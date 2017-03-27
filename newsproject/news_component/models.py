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
    NEWS_Mk = 5
    NEWS_KHAN = 6
    NEWS_DAILYDH = 7
    NEWS_HANSPORTS = 9
    NEWS_HANKYUNG = 10
    NEWS_FNNEWS = 11
    NEWS_HERALD = 12
    NEWS_KMIB = 13
    NEWS_NEWSDAILY = 14
    NEWS_GOOGLE = 15
    NEWS_OHMYNEWS = 16
    NEWS_NOCUT = 17
    NEWS_HANKOOKI = 18


    CHOICES_NEWS = (
        (NEWS_CHOSUN, '조선일보'),
        (NEWS_DONGA, '동아일보'),
        (NEWS_HANI, '한겨레'),
        (NEWS_JOINS, '중앙일보'),
        (NEWS_Mk, '매일경제'),
        (NEWS_KHAN, '경향신문'),
        (NEWS_DAILYDH, '데일리한국'),
        (NEWS_HANSPORTS, '스포츠한국'),
        (NEWS_HANKYUNG, '한국경제'),
        (NEWS_FNNEWS, '파이낸셜'),
        (NEWS_HERALD, '헤럴드'),
        (NEWS_KMIB, '국민일보'),
        (NEWS_NEWSDAILY, '뉴스데일리'),
        (NEWS_GOOGLE, '구글뉴스'),
        (NEWS_OHMYNEWS, '오마이뉴스'),
        (NEWS_NOCUT, '노컷뉴스'),
        (NEWS_HANKOOKI, '서울경제'),
    )

    CONTENT_NEWS_STR = {
        NEWS_CHOSUN: 'chosun',
        NEWS_DONGA: 'donga',
        NEWS_HANI: 'hani',
        NEWS_JOINS: 'joins',
        NEWS_Mk: 'mk',
        NEWS_KHAN: 'khan',
        NEWS_DAILYDH: 'dailydh',
        NEWS_HANSPORTS: 'hansports',
        NEWS_HANKYUNG: 'hankyung',
        NEWS_FNNEWS: 'fnnews',
        NEWS_HERALD: 'herald',
        NEWS_KMIB: 'kmib',
        NEWS_NEWSDAILY: 'newsdaily',
        NEWS_GOOGLE: 'google',
        NEWS_OHMYNEWS: 'ohmynews',
        NEWS_NOCUT: 'nocut',
        NEWS_HANKOOKI: 'hankooki'
    }

    """
    뉴스 섹션
    """
    SECTION_MAIN = 1
    SECTION_POPULAR = 2
    SECTION_POLITICS = 3
    SECTION_ECONOMY = 4
    SECTION_SOCIETY = 5
    SECTION_INTENATIONAL = 6
    SECTION_CULTURE = 7
    SECTION_IT = 8
    SECTION_SCIENCE = 9
    SECTION_SPORTS = 10
    SECTION_ENTERTAINMENT = 11
    SECTION_REALESTATE = 12
    SECTION_FINANCIAL = 13
    SECTION_LIFE = 14
    SECTION_HEALTH = 15
    SECTION_EDUCATION = 16
    SECTION_BOOK = 17
    SECTION_WOMAN = 18
    SECTION_TRAVEL = 19
    SECTION_GAME = 20
    SECTION_MEDIA = 21
    SECTION_OPINION = 22



    CHOICES_SECTION = (
        (SECTION_MAIN, '주요기사'),
        (SECTION_POPULAR, '인기기사'),
        (SECTION_POLITICS, '정치'),
        (SECTION_ECONOMY, '경제'),
        (SECTION_SOCIETY, '사회'),
        (SECTION_INTENATIONAL, '국제'),
        (SECTION_CULTURE, '문화'),
        (SECTION_IT, 'IT'),
        (SECTION_SCIENCE, '과학'),
        (SECTION_SPORTS, '스포츠'),
        (SECTION_ENTERTAINMENT, '연예'),
        (SECTION_REALESTATE, '부동산'),
        (SECTION_FINANCIAL, '금융'),
        (SECTION_LIFE, '생활'),
        (SECTION_HEALTH, '건강'),
        (SECTION_EDUCATION, '교육'),
        (SECTION_BOOK, '도서'),
        (SECTION_WOMAN, '여성'),
        (SECTION_TRAVEL, '여행'),
        (SECTION_GAME, '게임'),
        (SECTION_MEDIA, '미디어'),
        (SECTION_OPINION, '오피니언'),
    )

    CONTENT_SECTION_STR = {
        SECTION_MAIN: 'main',
        SECTION_POPULAR: 'popular',
        SECTION_POLITICS: 'politics',
        SECTION_ECONOMY: 'economy',
        SECTION_SOCIETY: 'society',
        SECTION_INTENATIONAL: 'intenational',
        SECTION_CULTURE: 'culture',
        SECTION_IT: 'it',
        SECTION_SCIENCE: 'science',
        SECTION_SPORTS: 'sports',
        SECTION_ENTERTAINMENT: 'entertainment',
        SECTION_REALESTATE: 'realestate',
        SECTION_FINANCIAL: 'financial',
        SECTION_LIFE: 'life',
        SECTION_HEALTH: 'health',
        SECTION_EDUCATION: 'education',
        SECTION_BOOK: 'book',
        SECTION_WOMAN: 'woman',
        SECTION_TRAVEL: 'travel',
        SECTION_GAME: 'game',
        SECTION_MEDIA: 'media',
        SECTION_OPINION: 'opinion'
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    news_company = models.IntegerField(choices=CHOICES_NEWS)
    xml_address = models.CharField(max_length=255)
    news_section = models.IntegerField(choices=CHOICES_SECTION)

    @property
    def get_section_name(self):
        return NewsContent.CHOICES_SECTION[self.news_section-1][1]

    @property
    def get_company_name(self):
        return NewsContent.CHOICES_NEWS[self.news_company-1][1]