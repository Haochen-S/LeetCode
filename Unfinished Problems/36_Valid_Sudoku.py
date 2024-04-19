# 36. Valid Sudoku


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if (not checkEachBox(board)):
            return False
        if (not checkEachColumn(board)):
            return False
        if (not checkEachRow(board)):
            return False

        return True

def checkEachBox(board):
    nineList = []
    row = 0
    column = 0

    i = 0
    # 0 1 2
    # 3 4 5
    # 6 7 8
    while (i < 9):
        j = 0
        nineList = []
        while (j < 9):
            nineList.append(board[row, column + j])
            j += 1 
        if (column < 6):
            column += 3
        else:
            column = 0
        i += 1
    return True        

def checkEachColumn(board):
    nineList = []
    return True

def checkEachRow(board):
    nineList = []
    return True
