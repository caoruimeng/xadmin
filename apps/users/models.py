from django.db import models

from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name=u'昵称', blank=True, null=True)
    age = models.IntegerField(verbose_name=u'年龄', blank=True, null=True)
    gender = models.CharField(max_length=10, choices=(('Female', u'女'), ('Male', '男')), verbose_name=u'性别', default='Male')

    class Meta:
        verbose_name = u'用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
