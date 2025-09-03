from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from django.utils import timezone
from .models import StreamSessions as StreamSession
from django.db import models
# Create your views here.
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def stream_url(request):
    """Return stream HLS URL (static for now)"""
    hls_url = f"http://{settings.STREAM_HOST}/hls/stream.m3u8"
    return Response({"url": hls_url})

@api_view(["POST"])
@permission_classes([IsAuthenticated])
def stream_start(request):
    """User starts watching → create session"""
    session = StreamSession.objects.create(user=request.user)
    return Response({"session_id": session.id})


@api_view(["POST"])
@permission_classes([IsAuthenticated])
def stream_stop(request):
    """User stops watching → close session"""
    session_id = request.data.get("session_id")
    try:
        session = StreamSession.objects.get(id=session_id, user=request.user, end_time__isnull=True)
        session.close()
        return Response({"message": "Session closed", "duration": session.duration})
    except StreamSession.DoesNotExist:
        return Response({"error": "No active session"}, status=400)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def analytics(request):
    """Return total watch duration for logged-in user"""
    total = StreamSession.objects.filter(user=request.user).aggregate(
        total=models.Sum("duration")
    )["total"] or 0
    return Response({"username": request.user.username, "watch_seconds": total})