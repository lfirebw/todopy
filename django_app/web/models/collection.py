from django.db import models
from django.utils import timezone
import uuid

class Collection(models.Model):
    unique_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    color = models.CharField(max_length=7, default="#FFFFFF")
    created = models.DateTimeField(default=timezone.now)