# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils.translation import gettext_lazy as _


class Subscriber(models.Model):
    '''
    Подписчик
    '''
    email = models.EmailField(
        verbose_name=_('e-mail'),
        null=False,
        blank=False,
        db_index=True
    )
    name = models.CharField(
        verbose_name=_('Name'),
        max_length=50,
        null=True,
        blank=False
    )
    last_name = models.CharField(
        verbose_name=_('Last Name'),
        max_length=50,
        null=True,
        blank=False
    )
    birth_date = models.DateField(
        verbose_name=_('Date of birth'),
        null=True,
        blank=False,
    )

    class Meta:
        verbose_name = _('Subscriber')
        verbose_name_plural = _('Subscribers')


# class MailLog(models.Model):
#     '''
#     Лог отправки
#     '''
#     is_sent = models.BooleanField(
#         verbose_name=_('Отправлено'),
#         default=True,
#         db_index=True
#     )
#     created = models.DateTimeField(
#         verbose_name=_('Дата создания'), 
#         auto_now_add=True
#     )
#     from_email = models.EmailField(
#         verbose_name=_('Отправитель'),
#         blank=True,
#         null=True
#     )
#     to_email = models.ForeignKey(
#         to=Subscriber,
#         null=True,
#         default=None,
#         on_delete=models.SET_DEFAULT
#     )
#     is_read = models.BooleanField(
#         verbose_name=_('Прочитано'),
#         default=False,
#         db_index=True
#     )

#     class Meta:
#         verbose_name = _('Лог')
#         verbose_name_plural = _('Логи')

#     def __str__(self):
#         return self.to_email
