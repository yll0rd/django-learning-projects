from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# Create your views here.

class UserListView(APIView):
    def get(self, request, format=None):
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)

class RegisterView(APIView):
    def post(self, request, format=None):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        
        if not username or not password or not email:
            return Response({'error': 'Please provide all required fields'})
        try:
            user = User.objects.create(username=username, password=password, email=email)
        except Exception as e:
            return Response({'error': str(e)})
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token, 'created': created})