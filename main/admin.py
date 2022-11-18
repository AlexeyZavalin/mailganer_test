# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Subscriber, MailLog


class SubscriberAdmin(admin.ModelAdmin):
    pass


class MailLogAdmin(admin.ModelAdmin):
    list_display = ('created', 'is_sent', 'to_email', 'is_read')


admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(MailLog, MailLogAdmin)
