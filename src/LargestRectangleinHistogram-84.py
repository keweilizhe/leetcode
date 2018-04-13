#! /usr/local/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import math
import json

import logging.handlers

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
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.


Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].


The largest rectangle is shown in the shaded area, which has area = 10 unit.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

'''

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        
        heights.append(0)
        stack = []
        max_area = 0

        for i in range(len(heights)):
            while len(stack) > 0 and heights[stack[len(stack)-1]] > heights[i]:
                site = stack.pop()
                if len(stack) > 0:
                    max_area = max(max_area, heights[site] * (i - stack[len(stack)-1] - 1))
                else:
                    max_area = max(max_area, heights[site] * i)

            stack.append(i)

        return max_area

heights = [2,1,5,6,2,3]
log.info(Solution().largestRectangleArea(heights))

