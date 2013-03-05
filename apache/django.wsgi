import os
import sys

activate_this = '/home/ubuntu/.virtualenvs/w4/bin/activate_this.py'
execfile(activate_this, dict(__file__=activate_this))

path = '/srv/www/w4/current/'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'theW4.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

