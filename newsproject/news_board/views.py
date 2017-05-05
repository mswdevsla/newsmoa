from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def notification(request):
    return render(request, 'news_board/notification.html', context={})

def user_board(request):
    return render(request, 'news_board/user_board.html', context={})

def board_write(request):

    return render(request, 'news_board/board_write.html', context={})