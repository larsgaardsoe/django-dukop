from .base import *  # noqa

DEBUG = True

# IP addresses marked as “internal” that can use the debug_toolbar
# https://docs.djangoproject.com/en/2.1/ref/settings/#internal-ips
INTERNAL_IPS = ["localhost", "127.0.0.1", "[::1]"]

# List of strings representing the host/domain names that this site can serve
# https://docs.djangoproject.com/en/2.1/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

INSTALLED_APPS += ("debug_toolbar",)  # noqa

COMPRESS_ENABLED = False

MIDDLEWARE = ["debug_toolbar.middleware.DebugToolbarMiddleware"] + MIDDLEWARE   # noqa

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

DEBUG_TOOLBAR_PATCH_SETTINGS = False
