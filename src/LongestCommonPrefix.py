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

Write a function to find the longest common prefix string amongst an array of strings.
        

1 找出最短的字符串长度
2 根据这个长度遍历每个字符串
        

'''

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        # min_len = -1
        # for s in strs:
        #     if min_len < 0:
        #         min_len = len(s)
        #         continue

        #     if min_len > len(s):
        #         min_len = len(s)
        # if min_len < 0:
        #     return result

        result = ''
        if len(strs) == 0:
            return result 

        s = strs[0]
        for i in range(len(s)):
            for p in strs:
                if len(p) <= i or p[i] != s[i]:
                    return result 
            result += s[i]

        return result


log.info(Solution().longestCommonPrefix(['aa', 'a']))

