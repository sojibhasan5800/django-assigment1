from django.db import models
from django.utils import timezone
# Create your models here.

class task_model(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField(default=timezone.now)
