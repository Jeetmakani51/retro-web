from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class GrindPost(models.Model):
    TAG_CHOICES = [
        ('grinding', 'grinding'),
        ('goal', 'goal'),
        ('quote', 'quote'),
        ('win', 'win'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=280)
    tag = models.CharField(max_length=20, choices=TAG_CHOICES, default='grinding')
    created_at = models.DateTimeField(auto_now_add=True)
    respect_count = models.PositiveBigIntegerField(default=0)

    class Meta:
        ordering = ['-created_at']