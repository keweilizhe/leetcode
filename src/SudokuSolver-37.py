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
Write a program to solve a Sudoku puzzle by filling the empty cells.

Empty cells are indicated by the character '.'.

You may assume that there will be only one unique solution.


[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]

遍历大九宫格, 

遇到数字记录3个有效表, 
遇到.符 开始尝试1-9
递归:
1. 尝试1-9, 行,列,小9宫格符合, 下一个
2. 1-9均不符合, 返回上一格, 换个数字开始遍历

'''

class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        def makeSudokuTable():
            return [ [0 for i in range(9)] for i in range(9)]

        row_valid = makeSudokuTable()
        column_valid = makeSudokuTable()
        little_sudoku_valid = makeSudokuTable()
        blank_list = [] #ele: (i,j) 空白的坐标列表
        result_lsit = []
        '''
        i = 1-3, j = 1-3, 第一个九宫格
        i = 1-3, j = 4-6, 第二个
        i = 4-6, j = 1-3, 第四个
        '''
        def getLittleSudokuNum(i, j):
            return (i//3) *3 + j//3

        def setValid(i, j, k, valid):
            row_valid[i][k] = valid
            column_valid[j][k] = valid
            little_sudoku_valid[getLittleSudokuNum(i,j)][k] = valid

        # 初始化检测数组, 空白位置坐标数组
        def iniSudokuTable():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        blank_list.append((i,j))
                        result_lsit.append(0)
                    else:
                        num = int(board[i][j]) - 1
                        setValid(i, j, num, 1)

        def checkValid(k, coordinate):
            i, j = coordinate
            if row_valid[i][k] == 1 or column_valid[j][k] == 1 or little_sudoku_valid[getLittleSudokuNum(i,j)][k] == 1:
                return False 
            return True



        def diguiSudoku(n):
            if n >= len(blank_list):
                return True

            i, j = blank_list[n][0], blank_list[n][1]
            for k in range(9):
                if checkValid(k, blank_list[n]):
                    setValid(i, j, k, 1)
                    result_lsit[n] = k + 1
                    if diguiSudoku(n+1): 
                        return True
                    setValid(i, j, k, 0)

            return False

        def modifyBoard(board):
            for n in range(len(blank_list)):
                i, j = blank_list[n]
                board[i][j] = str(result_lsit[n])
        
        iniSudokuTable()
        # log.info('blank_list = %s'%(blank_list))

        if diguiSudoku(0):
            modifyBoard(board)


def stringToChar2dArray(input):
    return json.loads(input)

def char2dArrayToString(input):
    return json.dumps(input)

sudoku = stringToChar2dArray('''[[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]''')

def main():
    pass
    Solution().solveSudoku(sudoku)
    log.info(sudoku)

if __name__ == '__main__':
    main()
