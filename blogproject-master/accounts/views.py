from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def sign_up(request):
    if request.method == 'POST':
        if request.POST['pw'] == request.POST['pw_confirm']:
            user = User.objects.create_user(
                request.POST['id'], password=request.POST['pw'])
            auth.login(request, user)
            return redirect('index')
    return render(request, 'sign_up.html')


#로그인의 예외상황을 같이 구현한 코드가 뭔가 이상하다

def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pw']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            return render(request, 'accounts/login.html')
    return render(request, 'login.html')

def logout(request):
    if request.method =='GET':
        auth.logout(request)
        return redirect('index')
    return render(request,'login.html')
