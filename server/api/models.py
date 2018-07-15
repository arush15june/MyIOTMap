from django.db.models.signals import post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User, Group
from django.db import models

from django.conf import settings

from api.helpers import GenerateUUID

class KeyValue(models.Model):
    key = models.CharField(max_length=200)
    value = models.CharField(max_length=400)

    def __str__(self):
        return '{}:{}'.format(self.key, self.value)

class DeviceData(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    recieved = models.ManyToManyField(
                        KeyValue
                    )        

class Device(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    uuid = models.CharField(
                        max_length=128, 
                        unique=True, 
                        blank=False, 
                        default=GenerateUUID
                    )
    data = models.ManyToManyField(
                        DeviceData
                    )