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

# file_handler = logging.handlers.RotatingFileHandler('log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)


'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

For example, given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = (n - 1) 
            
            sum_abc = -1
            while left < right:
                sum_abc = nums[i] + nums[left] + nums[right]

                if sum_abc > 0:
                    right -= 1
                elif sum_abc < 0:
                    left += 1
                else:
                    abc = [i, left, right]
                    abc.sort()
                    result.append([nums[abc[0]], nums[abc[1]], nums[abc[2]]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right + 1]: 
                        right -= 1


        log.info('len = %d, result = %s'%(len(result), str()))
        return (result) 



(Solution().threeSum(test))



[0,0,0,0,0,0]