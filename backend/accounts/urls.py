# accounts/urls.py

from django.urls import path
from .views import login_view, logout_view, check_login,get_csrf_token,get_user_info,register_user

urlpatterns = [
    path('login/', login_view),
    path('logout/', logout_view),
    path('check-login/', check_login),
    path('get_csrf_token/', get_csrf_token),
    path('user/', get_user_info, name='user-info'),
    path('register/', register_user, name='register'),
]
