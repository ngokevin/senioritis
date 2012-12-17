import os
import sys

os.environ['DJANGO_SETTINGS_MODULE'] = 'senioritis.settings'

path = '/home/ngoke/Code/'
if path not in sys.path:
    sys.path.append(path)

path = '/home/ngoke/Code/senioritis/'
if path not in sys.path:
    sys.path.append(path)

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()
