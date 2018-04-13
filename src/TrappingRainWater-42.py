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
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        length = len(height)
        left_max_height = [-1 for i in range(length)]
        right_max_height = [-1 for i in range(length)]

        for i in range(length):
            k = length - 1 -i
            if i == 0:
                left_max_height[i] = 0 #第一个元素左边没有
                right_max_height[k] = 0
                continue

            left_max_height[i] = max(left_max_height[i-1], height[i-1])
            right_max_height[k] = max(right_max_height[k+1], height[k+1])

        water = 0
        for i in range(length):
            current = min(left_max_height[i], right_max_height[i]) - height[i]
            if current > 0:
                water += current

        return water

def stringToIntegerList(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    pass
    height = [0,1,0,2,1,0,1,3,2,1,2,1]
    water = Solution().trap(height)
    log.info('water = %d'%(water))

if __name__ == '__main__':
    main()

