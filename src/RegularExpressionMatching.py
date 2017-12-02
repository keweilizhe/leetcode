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
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → False
isMatch("aa","aa") → True
isMatch("aaa","aa") → False
isMatch("aa", "a*") → True
isMatch("aa", ".*") → True
isMatch("ab", ".*") → True
isMatch("aab", "c*a*b") → True
'''


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        log.info('s = %s, p = %s'%(s, p))

        if len(p) == 0:
            return True if len(s) == 0 else False 
        elif len(p) == 1:
            if len(s) == 1 and (s[0] == p[0] or p[0] == '.'):
                return True 

            return False 

        else:
            if p[1] != '*':
                if len(s) > 0 and (s[0] == p[0] or p[0] == '.'):
                    return self.isMatch(s[1:], p[1:])

                return False
            else:
                if self.isMatch(s[0:], p[2:]):
                    return True

                i = 0
                while i < len(s) and (s[i] == p[0] or p[0] == '.'):
                    if self.isMatch(s[i+1:], p[2:]):
                        return True
                    i += 1

                return False


def check(s, p, result):
    if Solution().isMatch(s, p) != result:
        log.error("s = %s, p = %s, result should be %s"%(s, p, result))

# check("aa", "a", False)
# check("aa","aa", True) 
# check("aaa","aa", False) 
# check("aa", "a*", True) 
# check("aa", ".*", True) 
# check("ab", ".*", True) 
# check("aab", "c*a*b", True) 

# check("aaa", "a.a", True)
check("aa", ".", False)