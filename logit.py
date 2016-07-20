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
        resp = func(request, *args, **kwargs)
        try:
            logger.debug(resp.content)
        except Exception as e:
            logger.debug(e.message)
        return resp
    return with_logging
