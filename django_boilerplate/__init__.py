import logging
from django.conf import settings


APP_VERSION = '1.1'
__version__ = APP_VERSION
__alias__ = settings.APP_NAME

logger = logging.getLogger('base')

msg = "Starting '{}' v. {}".format(__alias__, __version__)
logger.debug(msg)
