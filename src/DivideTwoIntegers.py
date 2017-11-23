#! /usr/local/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import math

import logging.handlers

log     = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# file_handler = logging.handlers.RotatingFileHandler('demand.log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

'''
Divide two integers without using multiplication, division and mod operator.

If it is overflow, return MAX_INT.
'''


class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        MAX_INT = 0x7fffFFFF

        flag = (dividend ^ divisor) >> 31  # flag 0 表示正数, 1 表示负数
        a = abs(dividend)
        b = abs(divisor)
        if b == 0 :
            return MAX_INT

        if b > a:
            return 0

        k = 0
        while (b << k) < a:
            k += 1
        #log.info('k = %d'%(k))

        result = 0
        for i in range(k , -1, -1):
            #log.info('i = %d'%(i))
            if a >= (b << i):
                result += (1 << i)
                a -= (b << i)

        result = -result if flag else result
        if result > MAX_INT:
            return MAX_INT

        return result


log.info(Solution().divide(-2147483648, 1))


