from django.shortcuts import render
from newsproject.news_board.models import NewsBoard

from django.contrib.auth.decorators import login_required


def notification(request):
    news_boards = NewsBoard.objects.filter(mode=1).order_by('-id')
    mode = 1
    return render(request, 'news_board/notification.html', context={
        'news_boards': news_boards,
        'mode': mode
    })

def user_board(request):
    news_boards = NewsBoard.objects.filter(mode=2).order_by('-id')
    mode = 2
    return render(request, 'news_board/user_board.html', context={
        'news_boards': news_boards,
        'mode': mode
    })

@login_required
def board_write(request):
    if request.GET.get('mode'):
        mode = int(request.GET.get('mode'))
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        mode = int(request.POST.get('mode'))
        NewsBoard.objects.create(title=title, content=content, user_info=request.user.user_info, mode=mode)
        redirect_url = '/'
        if mode == 1:
            redirect_url = '/news_board/notification'
        elif mode == 2:
            redirect_url = '/news_board/user_board'
        from django.http import HttpResponseRedirect
        return HttpResponseRedirect(redirect_url)

    return render(request, 'news_board/board_write.html', context={
        'mode': mode
    })

def board_view(request, board_id):
    board = NewsBoard.objects.get(id=board_id)
    return render(request, 'news_board/board_view.html', context={
        'board': board
    })