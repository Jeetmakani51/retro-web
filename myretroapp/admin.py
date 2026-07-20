from django.contrib import admin
from .models import DailyAnswer, DailyPrompt
# Register your models here.

admin.site.register(DailyPrompt)
admin.site.register(DailyAnswer)
