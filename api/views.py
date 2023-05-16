# from django.shortcuts import render
from django.contrib.auth import login
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page, never_cache
from django.core.cache import cache
from django.db import connections, transaction
from rest_framework import views
from knox.views import LoginView as KnoxLoginView

from rest_framework import permissions, authentication, response
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.settings import api_settings

from api import models, serializers


class LoginView(KnoxLoginView):
    authentication_classes = (authentication.BasicAuthentication, )
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginView, self).post(request, format=None)


class ProductListView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    filter_backends = api_settings.DEFAULT_FILTER_BACKENDS
    filterset_fields = ['main_color', 'secondary_colors', 'brand']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)

        minpp = self.request.query_params.get('min_price', None)
        maxpp = self.request.query_params.get('max_price', None)

        if minpp is not None:
            queryset = queryset.filter(price__gte=float(minpp))

        if maxpp is not None:
            queryset = queryset.filter(price__lte=float(maxpp))

        return queryset

    @method_decorator(cache_page(60*5))
    def get(self, request, format=None):
        caps = models.Cap.objects.all().filter(
            is_deleted=False).order_by('-created_date')
        tshirts = models.TShirt.objects.all().filter(
            is_deleted=False).order_by('-created_date')

        caps = self.filter_queryset(caps)
        tshirts = self.filter_queryset(tshirts)

        cap_serializer = serializers.CapListSerializer(caps, many=True)
        tshirt_serializer = serializers.TShirtListSerializer(
            tshirts, many=True)

        data = cap_serializer.data + tshirt_serializer.data

        return response.Response(data)
