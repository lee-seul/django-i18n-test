# coding: utf-8


from django.db import models
from django.utils.translation import gettext as _


class HelloText(models.Model):
    text = models.CharField(max_length=100, verbose_name=_('hello'))

    def __str__(self):
        return self.text