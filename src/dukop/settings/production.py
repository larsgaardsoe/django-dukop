from .base import *  # noqa

MANAGERS = ADMINS = [
    ("Main admin team", "lol@dukop.dk")
]

DEFAULT_FROM_EMAIL = "dukop@riseup.net"

# For email, you wanna put something like this in production env's
# settings.local:
"""
EMAIL_HOST = config.get('mail', 'host')
EMAIL_PORT = config.get('mail', 'port')
EMAIL_HOST_USER = config.get('mail', 'user')
EMAIL_HOST_PASSWORD = config.get('mail', 'password')
EMAIL_USE_TLS = config.getboolean('mail', 'tls')
EMAIL_USE_SSL = config.getboolean('mail', 'ssl')
"""
