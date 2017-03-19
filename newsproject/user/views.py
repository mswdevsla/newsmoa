from django.shortcuts import render
# Create your views here.

def register(request):
    if request.method == 'POST':
        print(1)
    return render(request, 'user/register.html')