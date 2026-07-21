from django.contrib import admin
from .models import DailyAnswer, DailyPrompt, TimeCapsule
# Register your models here.

admin.site.register(DailyPrompt)
admin.site.register(DailyAnswer)
admin.site.register(TimeCapsule)