array = [[0,1,0,0,0],
[1,1,1,0,0],
[1,1,0,0,0],
[0,1,0,1,0]]

# [[0,1,0,0,0],
# [ 1,1,1,0,0],
# [ 1,1,0,0,0],
# [ 0,1,0,1,0]]


# 把目标相邻的 和目标拥有一样数字的index的值换成 target value

row = 1
column = 2
replace = 2

def solution(array, row, column, replace):
    targetElement = array[row][column]
    rowLen = len(array)
    colLen = len(array[0])
    
    replaceNum(array, row, column, targetElement, replace, rowLen, colLen)

    return array


def replaceNum(array, row, column, targetElement, replace, rowLen, colLen):
    if (array[row][column] == targetElement):
        array[row][column] = replace
    else:
        return

    if (row - 1 >= 0):
        replaceNum(array, row - 1, column, targetElement, replace, rowLen, colLen)
    if (row + 1 < rowLen):
        replaceNum(array, row + 1, column, targetElement, replace, rowLen, colLen)
    if (column - 1 >= 0):
        replaceNum(array, row, column - 1, targetElement, replace, rowLen, colLen)
    if (column + 1 < colLen):
        replaceNum(array, row, column + 1, targetElement, replace, rowLen, colLen)


for x in solution(array, row, column, replace):
    print(x)



