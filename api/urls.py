from django.urls import path, include
from rest_framework import routers
from knox import views as knox_views

from api import views

router = routers.DefaultRouter()

auth_urls = [
    path('login/', views.LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
]

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include(auth_urls)),
    path('', include(router.urls)),
]
