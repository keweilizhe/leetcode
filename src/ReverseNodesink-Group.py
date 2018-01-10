
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
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''

'''

如果能取k个节点, 颠倒这个K节点链表
不能取k个节点, return

k个元素的链表 

头结点head = p1, tail = p4, p1->p2->p3->p4
改为 head = p4, tail = p1  p1<-p2<-p3<-p4 

记录尾节点 tail
记录当前修改的左右节点 left, right, 
下次修改完毕后 更新左右节点
最后一次修改, 记录头结点, 更新tail.next 的值, 指向p4.next
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if k <= 1:
            return head

        def hasKNode(k, p):
            for i in range(k):
                if p == None:
                    return False 
                p = p.next

            return True

        # 返回 这k个节点中的头结点, 和尾节点
        def reverseKList(k, p):
            head = p
            tail = p

            left = p 
            right = p.next
            
            for i in range(k-1):
                next_node = right.next
                right.next = left
                
                if i < k - 2:
                    left = right
                    right = next_node
                else:
                    head = right
                    tail.next = next_node

            return head, tail
        
        p = head
        pre = None

        while p != None:
            if hasKNode(k, p) == False:
                break 

            if p == head:
                head, pre = reverseKList(k, p)
                p = pre.next
            else:
                pre.next, p = reverseKList(k, p)
                pre = p
                p = pre.next



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

def stringToInt(input):
    return int(input)

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():

    line = '[1,2,3,4,5]'
    k = 3

    head = stringToListNode(line)
    ret = Solution().reverseKGroup(head, k)

    out = listNodeToString(ret)
    log.info(out)

if __name__ == '__main__':
    main()








