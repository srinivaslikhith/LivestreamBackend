from django.urls import path
from . import views

urlpatterns = [
    path("api/register/", views.register, name="register"),
    path("stream_url/", views.stream_url, name="stream_url"),
    path("stream_start/", views.stream_start, name="stream_start"),
    path("stream_stop/", views.stream_stop, name="stream_stop"),
    path("analytics/", views.analytics, name="analytics"),
]