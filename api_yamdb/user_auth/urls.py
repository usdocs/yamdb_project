from django.urls import include, path
from rest_framework import routers

from user_auth.views import SignupViewSet, TokenViewSet

v1_router = routers.DefaultRouter()
v1_router.register('', SignupViewSet, basename='signup')
v1_router.register('', TokenViewSet, basename='token')

urlpatterns = [
    path('', include(v1_router.urls)),
]
