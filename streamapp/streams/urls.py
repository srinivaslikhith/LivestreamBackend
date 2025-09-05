from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", obtain_auth_token),
    path("stream_url/", views.stream_url, name="stream_url"),
    path("stream_start/", views.stream_start, name="stream_start"),
    path("stream_stop/", views.stream_stop, name="stream_stop"),
    path("analytics/", views.analytics, name="analytics"),
]