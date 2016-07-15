# -*- coding: utf-8 -*-

import logging
from functools import wraps


logger = logging.getLogger('logit')


def logit(func):
    @wraps(func)
    def with_logging(request, *args, **kwargs):
        logger.debug(func.__name__)
        try:
            logger.debug(request.body)
        except Exception as e:
            logger.debug(e.message)
        logger.debug(request.GET)
        logger.debug(request.POST)
        return func(request, *args, **kwargs)
    return with_logging
