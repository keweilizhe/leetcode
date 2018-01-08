#! /usr/local/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import math
import datetime
import logging.handlers
import json
import time

log     = logging.getLogger(__name__)
log.setLevel(logging.INFO)
log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# file_handler = logging.handlers.RotatingFileHandler('log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


'''

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []

        # left_num 左括号的余下数量,  right_num 右括号的余下数量
        def generateBracket(left_num, right_num, bracket_str):
            if left_num == 0 and right_num == 0 :
                result.append(bracket_str)
                return

            if left_num < right_num:
                if left_num > 0 :
                    generateBracket(left_num - 1, right_num, bracket_str + '(')
                if right_num > 0:
                    generateBracket(left_num, right_num - 1, bracket_str + ')')
            else:
                if left_num > 0 :
                    generateBracket(left_num - 1, right_num, bracket_str + '(')

        generateBracket(n, n, '')

        return result

if __name__ == '__main__':
    output = Solution().generateParenthesis(10)
    log.info('len = %s'%(len(output)))
    log.info('output = %s'%(output))



