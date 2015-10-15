"""
WSGI config for dj_page project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys

virtual_env = '/home/davel/repository/dj' 
activate_this = os.path.join(virtual_env, 'bin/activate_this.py')
execfile(activate_this, dict(__file__=activate_this))

sys.path.insert(0, '/home/davel/repository/dj/dj-page-news')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dj_page.settings")

application = get_wsgi_application()
