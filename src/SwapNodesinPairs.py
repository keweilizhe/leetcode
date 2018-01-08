
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
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        p = head 

        pre = None
        p1 = None 
        p2 = None 

        while p != None:
            p1 = p
            p2 = p.next

            if p2 != None :
                if p == head:
                    p1.next = p2.next
                    p2.next = p1
                    head = p2

                    pre = p1 
                    p = p1.next
                else:
                    p1.next = p2.next
                    p2.next = p1
                    pre.next = p2 

                    pre = p1 
                    p = p1.next 
            else:
                break

        return head



def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    # import sys
    # def readlines():
    #     for line in sys.stdin:
    #         yield line.strip('\n')
    line = '[1]'

    # line = lines.next()
    head = stringToListNode(line)
    log.info('head = %s, head.next = %s'%(head, head.next))

    ret = Solution().swapPairs(head)

    log.info('ret = %s'%(ret))
    out = listNodeToString(ret)
    log.info(out)

if __name__ == '__main__':
    main()


