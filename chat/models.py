from datetime import datetime

from django.db import models


# Create your models here.
class Chat(models.Model):
    class Meta:
        db_table = "chat"
        managed = True

    chat_id = models.CharField(max_length=60, null=False)
    sender = models.CharField(max_length=10, null=False)
    receiver = models.CharField(max_length=10, null=False)
    content = models.CharField(max_length=255, null=False)
    read = models.BooleanField(null=False, default=False)
    create_time = models.DateTimeField(auto_now=True)
