from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import logout
from . import views

def home(request):
    return render(request, 'accounts/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
            return render(request, 'login.html')  # 수정된 부분
    else:
        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    return redirect('login_view')  


def password_reset(request):
    return render(request, 'accounts/password_reset.html')



