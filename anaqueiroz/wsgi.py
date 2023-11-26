"""
WSGI config for anaqueiroz project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""


# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/username/mysite'
# and your manage.py is is at '/home/amaanx/mysite/manage.py'
path = '/home/anaqueiroz/anaqueiroz' 
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'anaqueiroz.settings' 

# then:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
