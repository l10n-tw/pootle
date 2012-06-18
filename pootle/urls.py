#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2008-2009 Zuza Software Foundation
#
# This file is part of Pootle.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, see <http://www.gnu.org/licenses/>.

from django.conf.urls.defaults import *
from django.conf import settings
from os import path

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

DJANGO_MEDIA = path.join(path.dirname(admin.__file__), 'media')

urlpatterns = patterns('',
    # Uncomment the next line to enable the admin:
    (r'^django_admin/', include(admin.site.urls)),

    # Static and media files
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^(favicon.ico)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': DJANGO_MEDIA}),

    # Direct download of translation files
    (r'^export/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.PODIRECTORY}),

    # Documentation
    (r'^docs/(?P<docfile>.*)$', 'django.views.generic.simple.direct_to_template', {'template': "docs.html"}),

    # External apps
    (r'^contact/', include('contact_form_i18n.urls')),
    (r'^accounts/', include('pootle_profile.urls')),

    # Pootle URLs
    (r'^about/', include('legalpages.urls')),
    (r'^projects/', include('pootle_project.urls')),
    (r'', include('pootle_notifications.urls')),
    (r'', include('pootle_terminology.urls')),
    (r'', include('pootle_store.urls')),
    (r'', include('pootle_app.urls')),
    (r'', include('pootle_translationproject.urls')),
    (r'', include('pootle_language.urls')),
)
