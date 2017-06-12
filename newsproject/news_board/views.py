from django.shortcuts import render
from newsproject.news_board.models import NewsBoard

from django.contrib.auth.decorators import login_required


def notification(request):
    news_boards = NewsBoard.objects.all().order_by('-id')
    return render(request, 'news_board/notification.html', context={
        'news_boards': news_boards
    })

def user_board(request):
    return render(request, 'news_board/user_board.html', context={})

def board_write(request):

    return render(request, 'news_board/board_write.html', context={})

def board_view(request, board_id):
    board = NewsBoard.objects.get(id=board_id)
    return render(request, 'news_board/board_view.html', context={
        'board': board
    })