# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.sites.models import Site
from django.core import signing
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template

from main.models import MailLog

from smtplib import SMTPException


def create_message_body(subscriber, message_id, template_name, content=None):
    '''
        Create body of mail
        subscriber: Subscriber
        message_id: MailLog.pk
        template_name: path to templates in templates dir
        content: content to render inside template
    '''
    domain = Site.objects.get_current().domain
    encrypted = signing.dumps(message_id, compress=True)
    path = '/mail_read_tracker/{}'.format(encrypted)
    url = 'http://{}{}'.format(domain, path)
    template = get_template(template_name)
    context = {
        'subscriber': subscriber,
        'track_url': url,
        'content': content
    }
    content = template.render(context)
    return content


def track_email(encrypted):
    '''
        email tracking
        encrypted: encrypted MailLog.pk
    '''
    try:
        mail_log = MailLog.objects.get(pk=signing.loads(encrypted))
        mail_log.is_read = True
        mail_log.save()
    except MailLog.DoesNotExist:
            pass


def send_mail(subscriber, template_name, subject, content=None):
    '''
        sending email
        Create body of mail
        subscriber: Subscriber
        template_name: path to templates in templates dir
        content: content to render inside template
    '''
    mail_log = MailLog.objects.create(
        from_email=settings.EMAIL_FROM,
        to_email=subscriber
    )
    body = create_message_body(subscriber, mail_log.pk, template_name, content)
    msg = EmailMultiAlternatives(subject, '', settings.EMAIL_FROM, [subscriber.email])
    msg.attach_alternative(body, "text/html")
    try:
        msg.send()
        mail_log.is_sent = True
        mail_log.save()
    except SMTPException:
        pass