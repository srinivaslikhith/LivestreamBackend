from django.urls import path
from . import views

urlpatterns = [
    path("stream-url/", views.stream_url, name="stream_url"),
    path("stream/start/", views.stream_start, name="stream_start"),
    path("stream/stop/", views.stream_stop, name="stream_stop"),
    path("analytics/", views.analytics, name="analytics"),
]