from django.db import models
from django.utils import timezone
from catagory.models import catagory_model
# Create your models here.

class task_model(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField()
    is_completed = models.BooleanField(default=False)
    assign_date = models.DateTimeField(default=timezone.now)
    catagory_name = models.ManyToManyField(catagory_model)
