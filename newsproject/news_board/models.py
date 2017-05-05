from django.db import models
from newsproject.user.models import UserInfo

# Create your models here.

class NewsBoard(models.Model):
    MODE_NOTIFICATION = 1
    MODE_BOARD = 2

    CHOICES_BOARD = (
        (MODE_NOTIFICATION, '공지사항'),
        (MODE_BOARD, '자유게시판')
    )

    BOARD_NEWS_STR = {
        MODE_NOTIFICATION: 'notification',
        MODE_BOARD: 'board'
    }

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=256)
    content = models.TextField()
    user_info = models.OneToOneField(UserInfo, null=True, on_delete=models.SET_NULL, related_name='user_info')
    mode = models.IntegerField(choices=CHOICES_BOARD)
