from django.db import models
from django.utils import timezone
from .collection import Collection
import uuid

class Task(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    text = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    checked = models.BooleanField(default=False)
    collection = models.ForeignKey(Collection, on_delete=models.SET_NULL, null=True, blank=True)
    created = models.DateTimeField(default=timezone.now)