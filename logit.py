# -*- coding: utf-8 -*-

from functools import wraps


import logging


logger = logging.getLogger('logit')


def logit(func):
    @wraps(func)
    def with_logging(request, *args, **kwargs):
        logger.debug(func.__name__)
        logger.debug(request.GET)
        logger.debug(request.POST)
        return func(request, *args, **kwargs)
    return with_logging
