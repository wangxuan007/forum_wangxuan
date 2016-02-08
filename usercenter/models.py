# coding:utf-8
from django.contrib.auth.models import User
from django.db import models


class ActivateCode(models.Model):
    owner = models.ForeignKey(User, verbose_name="用户")
    code = models.CharField(u"激活码", max_length=1000)

    expire_timestamp = models.DateTimeField()

    creat_timestamp = models.DateTimeField(auto_now_add=True)
    last_update_timestamp = models.DateTimeField(auto_now_add=True)
