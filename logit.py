# -*- coding: utf-8 -*-

import logging
from functools import wraps


logger = logging.getLogger('logit')


def loggerit(func, flag, content):
    logger.debug('func=%s&flag=%s&content=%s', func, flag, content)


def logit(func):
    @wraps(func)
    def with_logging(request, *args, **kwargs):
        # 获取函数名
        name = func.__name__
        # 打印 body 内容到日志文件
        try:
            loggerit(name, 'body', request.body)
        except Exception as e:
            loggerit(name, 'error', e.message)
        # 打印 get 内容到日志文件
        loggerit(name, 'get', request.GET)
        # 打印 POST 内容到日志文件
        loggerit(name, 'post', request.POST)
        res = func(request, *args, **kwargs)
        # 打印 response 内容到日志文件
        try:
            loggerit(name, 'res', res.content)
        except Exception as e:
            loggerit(name, 'error', e.message)
        return res
    return with_logging
