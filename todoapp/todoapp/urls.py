"""
URL configuration for todoapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from accounts import views
from todo import views as todo_views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # 추가
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('todo_list/', views.todo_list, name='todo_list'),
    path('test_message/', views.test_message, name='test_message'),
    path('__debug__/', include('debug_toolbar.urls')),
    path('<int:pk>/', todo_views.todo_detail, name='todo_detail'),
    path('todo_detail/', todo_views.todo_detail, name='todo_detail')
]