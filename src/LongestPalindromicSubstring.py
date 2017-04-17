#! /usr/local/bin/python3
#-*-coding:utf-8-*-


import os
import sys

import datetime
import time
import math
import decimal
import json

import copy

import pymysql
import logging.handlers

import smtplib
from email.mime.text import MIMEText
from email.header import Header

log     = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')
# file_handler = logging.handlers.RotatingFileHandler('demand.log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)


def longestPalindrome(s):

    s1 = '^#' + '#'.join(s) + '#$'
    log.info('s1=' + s1)

    RL = [0] * len(s1)
    MaxRight = 0
    pos = 0

    for i in range(len(s1)):
        if (i < MaxRight):
            RL[i] = min(RL[pos - (i-pos)], MaxRight - i)
        else:
            RL[i] = 0;

        #  注意边界两边都有, 不能只考虑右边界
        while i - RL[i]-1 >= 0 and i + RL[i]+1 < len(s1) and s1[i - RL[i]-1] == s1[i + RL[i]+1]:
            RL[i] += 1

        if (RL[i] + i > MaxRight):
            pos = i
            MaxRight = RL[i] + i

    center = 0
    maxlen = 0
    for i in range(len(RL)):
        if RL[i] > maxlen:
            maxlen = RL[i]
            center = i

    start = int((center - 1 - maxlen)/2)
    end = int((center - 1 - maxlen)/2+maxlen)
    return s[start : end]

log.info(longestPalindrome('ccbbaaabba'));

# ['a','b','b','a']