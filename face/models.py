from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=32)
    published_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='profile_pics/')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title



