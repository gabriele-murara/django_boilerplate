import logging

APP_VERSION = '1.0'
__version__ = APP_VERSION
__alias__ = 'Django Boilerplate'

logger = logging.getLogger('base')

msg = "Starting '{}' v. {}".format(__alias__, __version__)
logger.debug(msg)
