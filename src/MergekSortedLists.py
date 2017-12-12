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
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.


'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        klist = [] # {'value':x, 'list_num':y}
        for i in range(len(lists)):
            # log.info('l = %s'%(str(l)))
            if lists[i] != None:
                klist.append({'value':lists[i].val, 'list_num':i})
                lists[i] = lists[i].next

        def less(x, y):
            return x['value'] < y['value']
        def key(v):
            return v['value']

        klist.sort(key = key)
        # log.info('klist = %s'%(str(klist)))

        head = ListNode(None)
        tail = head
        def insert(l, v):
            left = 0
            right = len(l) - 1

            while left <= right:

                mid = (left + right) // 2
                if less(l[mid], v):
                    left = mid + 1
                else:
                    right = mid - 1
            l.insert(left, v)

        while len(klist) > 0:
            val = klist[0]['value']
            list_num = klist[0]['list_num']
            log.info('klist = %s'%(str(klist)))
            node = ListNode(val)
            tail.next = node
            tail = tail.next
            klist.pop(0)

            l = lists[list_num]

            if l != None:
                insert(klist, {'value':l.val, 'list_num':list_num})
                lists[list_num] = lists[list_num].next
            # time.sleep(1)

        return head.next

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

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

def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

if __name__ == '__main__':
    input = '[[0,2,5]]'
    head = Solution().mergeKLists(stringToListNodeArray(input))
    log.info('output = %s'%(listNodeToString(head)))
