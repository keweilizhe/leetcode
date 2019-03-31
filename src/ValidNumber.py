#! /usr/local/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import math
import datetime
import logging.handlers

log     = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# file_handler = logging.handle.rs.RotatingFileHandler('log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

'''

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0": True
" 0.1 ": True
"abc": False
"1 a": False
"2e10": True
" -90e3   ": True
" 1e": False
"e3": False
" 6e-1": True
" 99e2.5 ": False
"53.5e93": True
" --6 ": False
"-+3": False
"95a54e53": False

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one. However, here is a list of characters that can be in a valid decimal number:

Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''

'''
分段表示法, 可允许的字符:

[N个空格][可有可无一个+-号][0123456789][.+01234566789][e+0123456789][空格]
'''

class Solution:
    def isNumber(self, s: str) -> bool:
        import re
        patt = re.compile(r"^ *[+-]?(\d+(\.?)|\.\d+)\d*(e[+-]?\d+)? *$")

        return bool(patt.match(s))

# print(Solution().isNumber(" +0000.e0 "))

ret_dict = {
    "0": True,
    " 0.1 ": True,
    "abc": False,
    "1 a": False,
    "2e10": True,
    " -90e3   ": True,
    " 1e": False,
    "e3": False,
    " 6e-1": True,
    " 99e2.5 ": False,
    "53.5e93": True,
    " --6 ": False,
    "-+3": False,
    "95a54e53": False,
    ".1": True,
    "3.": True,
}

for s, r in ret_dict.items():
    if bool(Solution().isNumber(s)) != r:
        log.info("not valid, s = %s, r = %s", s, r)
