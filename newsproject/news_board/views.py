from django.shortcuts import render
from newsproject.news_board.models import NewsBoard

from django.contrib.auth.decorators import login_required


def board_list(request):
    if request.GET.get('mode'):
        mode = request.GET.get('mode')
    else:
        mode = 2
    news_boards = NewsBoard.objects.filter(mode=mode).order_by('-id')
    title_str = NewsBoard.CHOICES_BOARD[int(mode)-1][1]
    return render(request, 'news_board/board_list.html', context={
        'news_boards': news_boards,
        'title_str': title_str
    })


@login_required
def board_write(request):
    previous_url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('mode'):
            title = request.POST.get('title')
            content = request.POST.get('content')
            mode = request.POST.get('mode')
            if (mode == 1 or mode == 3) and not request.user.user_info.is_admin_user:
                from django.http import HttpResponse
                return HttpResponse('<script>alert("접근 권한이 없습니다."); history.back();</script>')
            NewsBoard.objects.create(title=title, content=content, user_info=request.user.user_info, mode=mode)
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('list?mode=' + mode)
        else:
            from django.http import HttpResponse
            return HttpResponse('<script>alert("모든 값이 채워지지 않았습니다"); history.back();</script>')

    board_category = NewsBoard.CHOICES_BOARD
    return render(request, 'news_board/board_write.html', context={
        'board_category': board_category,
        'previous_url': previous_url
    })


def board_view(request, board_id):
    try:
        board = NewsBoard.objects.get(id=board_id)
        board.view_count = board.view_count + 1
        board.save()
    except NewsBoard.DoesNotExist:
        from django.http import HttpResponse
        HttpResponse('<script>alert("해당 게시글이 존재하지 않습니다"); history.back();</script>')
    return render(request, 'news_board/board_view.html', context={
        'board': board
    })


def board_modify(request, board_id):
    try:
        board = NewsBoard.objects.get(id=board_id)
        board.view_count = board.view_count + 1
        board.save()
    except NewsBoard.DoesNotExist:
        from django.http import HttpResponse
        HttpResponse('<script>alert("해당 게시글이 존재하지 않습니다"); history.back();</script>')

    if request.method == 'POST':
        if request.POST.get('title') and request.POST.get('content') and request.POST.get('mode'):
            title = request.POST.get('title')
            content = request.POST.get('content')
            mode = request.POST.get('mode')
            if (mode == 1 or mode == 3) and not request.user.user_info.is_admin_user:
                from django.http import HttpResponse
                return HttpResponse('<script>alert("접근 권한이 없습니다."); history.back();</script>')
            NewsBoard.objects.create(title=title, content=content, user_info=request.user.user_info, mode=mode)
            from django.http import HttpResponseRedirect
            return HttpResponseRedirect('/news_board/list?mode=' + mode)
        else:
            from django.http import HttpResponse
            return HttpResponse('<script>alert("모든 값이 채워지지 않았습니다"); history.back();</script>')

    board_category = NewsBoard.CHOICES_BOARD
    return render(request, 'news_board/board_modify.html', context={
        'board': board,
        'board_category': board_category
    })