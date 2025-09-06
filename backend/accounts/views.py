# accounts/views.py

from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token

 # ❗ if you're testing locally only; remove in production
@api_view(['POST'])
def login_view(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return Response({
            'message': 'Login successful',
            'user': {
                'username': user.username,
                'email': user.email
            }
        })

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({'message': 'Logged out'})

@api_view(['GET'])
def check_login(request):
    if request.user.is_authenticated:
        return Response({
            'isAuthenticated': True,
            'username': request.user.username  # 👈 make sure this is returned
        })
    return Response({'isAuthenticated': False})

@ensure_csrf_cookie
@api_view(['GET'])
def get_csrf_token(request):
    return Response({'csrftoken': get_token(request)})



    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_info(request):
    return Response({"username": request.user.username})

@api_view(['POST'])
def register_user(request):
    data = request.data
    if data['password'] != data['password2']:
        return Response({'error': 'Passwords do not match'}, status=400)

    if User.objects.filter(username=data['username']).exists():
        return Response({'error': 'Username already exists'}, status=400)

    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password']
    )
    return Response({'message': 'User created successfully'}, status=201)