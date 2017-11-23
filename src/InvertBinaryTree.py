#! /usr/local/bin/python3
#-*-coding:utf-8-*-


import os
import sys
import math

import logging.handlers

# log     = logging.getLogger(__name__)
# log.setLevel(logging.INFO)
# log_formatter = logging.Formatter(fmt='[%(asctime)s %(filename)s:%(funcName)s:%(lineno)s][%(levelname)s]:%(message)s',datefmt='%Y-%m-%d %H:%M:%S')

# file_handler = logging.handlers.RotatingFileHandler('demand.log.%s'%(str(datetime.date.today().strftime('%Y%m%d'))), maxBytes = 500 * 1024 * 1024, backupCount = 10)
# file_handler.setFormatter(log_formatter)
# log.addHandler(file_handler)

# stream_handler = logging.StreamHandler()
# stream_handler.setFormatter(log_formatter)
# log.addHandler(stream_handler)


'''

Invert a binary tree.

     4
   /   \
  2     7
 / \   / \
1   3 6   9
to
     4
   /   \
  7     2
 / \   / \
9   6 3   1

'''



# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root != None :
            temp = root.right
            root.right = root.left
            root.left = temp

            if root.left != None:
                root.left = self.invertTree(root.left)

            if root.right != None:
                root.right = self.invertTree(root.right)

        return root 

def stringToTreeNode(input):
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def treeNodeToString(root):
    output = ""
    queue = [root]
    length = 1
    current = 0
    while current != length:
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(output.left)
        queue.append(output.right)
    return "[" + output[:-2] + "]"

import sys
def readlines():
    for line in sys.stdin:
        yield line.strip('\n')

def main():
    lines = readlines()
    while True:
        try:
            line = lines.next()
            root = stringToTreeNode(line)
            
            ret = Solution().invertTree(root)

            out = treeNodeToString(ret)
            print (out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()







