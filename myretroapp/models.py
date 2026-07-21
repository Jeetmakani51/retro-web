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

class GrindComment(models.Model):
    post = models.ForeignKey(GrindPost, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

class DailyPrompt(models.Model):
    question = models.CharField(max_length=280)
    date = models.DateField(unique=True)

    def __str__(self):
        return f"{self.date}: {self.question}"


class DailyAnswer(models.Model):
    prompt = models.ForeignKey(DailyPrompt, on_delete=models.CASCADE, related_name='answers')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=280)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('prompt', 'user')  # one answer per user per prompt

class TimeCapsule(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_capsules')
    recipient = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='received_capsules',
        null=True, blank=True  # blank = message to your own future self
    )
    content = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    unlock_date = models.DateField()
    opened = models.BooleanField(default=False)

    class Meta:
        ordering = ['unlock_date']