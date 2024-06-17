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
            if user is not None:
                login(request, user)
                return redirect('todo_list')  
            else:
                messages.error(request, '사용자 인증에 실패했습니다.')
                return render(request, 'accounts/signup.html', {'form': form})
        else:
            messages.error(request, '폼이 유효하지 않습니다. 다시 시도해 주세요.')
    form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

# accounts/views.py
import logging
logger = logging.getLogger(__name__)

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                logger.debug(f'Login successful for user: {username}')
                return redirect('todo_list')  # URL 이름 확인 필요
            else:
                messages.error(request, '사용자 인증에 실패했습니다.')
                logger.debug(f'User authentication failed for user: {username}')
        else:
            messages.error(request, 'Invalid username or password.')
            logger.debug(f'Invalid form data for user: {request.POST.get("username")}')
    else:
        form = AuthenticationForm()
        logger.debug('GET 요청')

    return render(request, 'accounts/login.html', {'form': form})
    
def logout_view(request):
    logout(request)
    return redirect('login_view')  


def password_reset(request):
    return render(request, 'accounts/password_reset.html')

def todo_list(request):
    return render(request, 'todo/todo_list.html')

def test_message(request):
    messages.success(request, '성공 메시지 테스트입니다.') 
    return render(request, 'accounts/test_message.html')