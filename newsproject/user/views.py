from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.http import HttpResponseRedirect, HttpResponse
from newsproject.user.models import UserInfo
# Create your views here.

def register(request):
    if request.method == 'POST':
        if request.POST.get('password') == request.POST.get('re_password'):
            print(1)
            email = request.POST.get('email')
            id = request.POST.get('id')
            password = request.POST.get('password')
            try:
                User.objects.get(username=id)
                return HttpResponse('<script>alert("이미 존재하는 아이디입니다"); history.back();</script>')
            except User.DoesNotExist:
                pass
            try:
                User.objects.get(email=email)
                return HttpResponse('<script>alert("이미 존재하는 이메일입니다"); history.back();</script>')
            except User.DoesNotExist:
                pass

            user = User.objects.create_user(username=id, email=email, password=password)
            UserInfo.objects.create(user=user, email=email)
            print(1)
            return HttpResponseRedirect('/')
    return render(request, 'user/register.html')

def login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('user_id'), password=request.POST.get('user_password'))
        if user is not None:
            if user.is_active:
                auth_login(request, user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponse('<script>alert("Non active user");</script>')
        else:
            return HttpResponse('<script>alert("Wrong username or password");history.back();</script>')
    return render(request, 'user/login.html')

def logout(request):
    try:
        auth_logout(request)
        return HttpResponseRedirect('/')
    except:
        return HttpResponse('<script>alert("Some error occured.");history.back();</script>')