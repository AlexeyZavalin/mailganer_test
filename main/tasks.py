# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from celery import shared_task

from .models import Subscriber
from .services import send_mail

import datetime


@shared_task 
def daily_mail():
    subs = Subscriber.objects.filter(is_active=True)
    for sub in subs:
        send_mail(sub, 'daily_mail.html', 'Daily mail', datetime.datetime.now())
