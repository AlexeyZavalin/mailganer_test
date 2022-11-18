# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.http import HttpResponse

import services




def mail_read_tracker(request, encrypted):
    services.track_email(encrypted)
    return HttpResponse(
        content=settings.TRACK_IMAGE[1],
        content_type=settings.TRACK_IMAGE[0],
    )
