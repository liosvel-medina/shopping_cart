# from django.shortcuts import render
from django.contrib.auth import login
from django.contrib.auth.models import User
from rest_framework import views
from knox.views import LoginView as KnoxLoginView

from rest_framework import permissions, authentication, response
from rest_framework.authtoken.serializers import AuthTokenSerializer


class LoginView(KnoxLoginView):
    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)
