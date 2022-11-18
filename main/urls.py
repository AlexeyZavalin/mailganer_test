from django.conf.urls import url

from .views import mail_read_tracker

urlpatterns = [
    url(r'^mail_read_tracker/(.*?)/$',
        mail_read_tracker, name='mail-tracker'),
]