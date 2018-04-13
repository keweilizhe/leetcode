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
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

For example:
Given array A = [2,3,1,1,4]

The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

Note:
You can assume that you can always reach the last index.

'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # goal = len(nums) - 1 # target
        # # site = 0 # first place
        # self.current_min_step = -1 

        # def goNext(site, step):
            
        #     if site >= goal:
        #         # log.info('ok')
        #         if self.current_min_step < 0:
        #             self.current_min_step = step
        #         else:
        #             self.current_min_step = min(step, self.current_min_step)
        #         return True

        #     possible_step = min(nums[site], goal-site)
        #     # log.info('goal=%d, site=%d, step=%d, possible_step=%d'%(goal, site, step, possible_step))
        #     for i in range(1, possible_step+1):
        #         k = possible_step + 1 - i
        #         goNext(site+k, step+1)

        # goNext(0, 0)
        # return self.current_min_step

        ret = 0;
        last = 0;
        curr = 0;
        for i in range(len(nums)):
            if i > last:
                last = curr;
                ret += 1;
            
            curr = max(curr, i+nums[i]);
            # log.info('i = %d, curr = %d, last = %d'%(i, curr, last))

        return ret;



A = [6,2,6,1,7,9,3,5,3,7,2,8,9,4,7,7,2,2,8,4,6,6,1,3]

log.info(Solution().jump(A))
