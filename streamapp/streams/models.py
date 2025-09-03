from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class StreamSessions(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    starttime = models.DateTimeField(default=timezone.now)
    endtime = models.DateTimeField(null=True, blank=True) 
    duration = models.DurationField(default = 0)

    def close(self):
        self.endtime = timezone.now()
        self.duration = int((self.endtime - self.starttime).total_seconds())
        self.save()

