#! /usr/local/bin/python3
#-*-coding:utf-8-*-

import os
import sys
import math
import json

import logging.handlers

log     = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# file_handler = logging.handlers.RotatingFileHandler('log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(log_formatter)
log.addHandler(stream_handler)

'''
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # returns 1
cache.put(3, 3);    # evicts key 2
cache.get(2);       # returns -1 (not found)
cache.put(4, 4);    # evicts key 1
cache.get(1);       # returns -1 (not found)
cache.get(3);       # returns 3
cache.get(4);       # returns 4

'''

class LRUCache:

    class ListNode():
        def __init__(self, x, y):
            self.key = y
            self.val = x
            self.next = None
            self.pre = None

    class DoubleList():
        def __init__(self):
            self.head = LRUCache.ListNode(-1, -1)
            self.tail = self.head

        def insert(self, node):
            # if self.tail == None:
            #     self.head.next = node
            #     node.pre = self.head
            #     self.tail = node
            #     node.next = None
            # else:
                self.tail.next = node
                node.pre = self.tail
                node.next = None
                self.tail = node
                self.print()

        def update(self, node):
            if self.tail == node:
                return

            node.pre.next = node.next
            node.next.pre = node.pre

            self.tail.next = node
            node.pre = self.tail
            node.next = None
            self.tail = node

            log.info('head = %d, tail = %d'%(self.head.next.key, self.tail.key))
            self.print()

        def delete(self):
            log.info('head next = %s'%(self.head.next))
            # if self.head.next != None:
            node = self.head.next
            self.head.next = self.head.next.next

            if self.head.next == None:
                self.tail = self.head
            else:
                self.head.next.pre = self.head

            self.print()
            return node.key

        def print(self):
            node = self.head.next
            l = []

            while node != None:
                l.append([node.key, node.val])
                node = node.next

            log.info(l)

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.tb = {}  # k:v = key : listNode
        self.list = LRUCache.DoubleList()

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.tb: 
            node = self.tb[key]
            self.list.update(node)

            return node.val

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.tb:
            node = self.tb[key]
            node.val = value
            self.list.update(node)
        else:
            if len(self.tb) >= self.capacity:
                old_key = self.list.delete()
                del self.tb[old_key]

            self.tb[key] = LRUCache.ListNode(value, key)
            self.list.insert(self.tb[key])

        self.list.print()


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

# cache = LRUCache(2);

# (cache.put(1, 1));
# (cache.put(2, 2));
# log.info(cache.get(1));       # returns 1
# (cache.put(3, 3));    # evicts key 2
# log.info(cache.get(2));       # returns -1 (not found)
# (cache.put(4, 4));    # evicts key 1
# log.info(cache.get(1));       # returns -1 (not found)
# log.info(cache.get(3));       # returns 3
# log.info(cache.get(4));       # returns 4

["LRUCache","put","get","put","get","get"]
[[1],[2,1],[2],[3,2],[2],[3]]
func = ["put","get","put","get","get"]
kv = [[2,1],[2],[3,2],[2],[3]]

cache = LRUCache(1);

for i in range(len(func)):

    log.debug('tb key = %s'%([x for x in cache.tb]))
    log.debug('kv = %s'%(kv[i]))

    if func[i] == "put":
        cache.put(kv[i][0], kv[i][1])
    else:
        log.info(cache.get(kv[i][0]))

