from django.db import models


# Create your models here.


class User(models.Model):
    class Meta:
        managed = True
        db_table = 'user'

    username = models.CharField(max_length=30, null=False)
    type = models.CharField(choices=((1, 'manager'), (2, 'employee')), max_length=10, default=2)
    password = models.CharField(max_length=60, null=False)
    position = models.CharField(max_length=15, null=False, default="Unknown")
    avatar = models.CharField(max_length=8, null=False, default="ava1")
    motto = models.CharField(max_length=50, null=True)
