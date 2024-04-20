# 1992. Find All Groups of Farmland

class Solution(object):
    def findFarmland(self, land):
        """
        :type land: List[List[int]]
        :rtype: List[List[int]]
        """
        return numIslands(land)

# find the corner of the island
def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    lands = []
    numOfLayers = len(grid)
    numOfElements = len(grid[0])
    i = 0
    while (i < numOfLayers):
        j = 0

        while (j < numOfElements):
            left = False
            top = False
            if (grid[i][j] == 0):
                j += 1
                continue
        
            # if most top
            if (i == 0):
                top = True
            elif (grid[i-1][j] == 0):
                top = True
                
            # most left
            if (j == 0):
                left = True
            elif (grid[i][j-1] == 0):
                left = True

            # check if its the island's corner
            if (left and top):
                lands.append([i,j] + clearNeighbor(grid, i, j, numOfLayers, numOfElements))
                print(clearNeighbor(grid, i, j, numOfLayers, numOfElements))
            j += 1
        i += 1

    return lands


# return list [topLeft, Top, Bot, BotRight]
def clearNeighbor(grid, i, j, numOfLayers, numOfElements):
    ans = [i, j]

    if (i+1 < numOfLayers):
        if (grid[i+1][j] != 0):
            ans = clearNeighbor(grid, i+1, j, numOfLayers, numOfElements)
            i = ans[0]
    else:
        ans = [i, j]

    if (j+1 < numOfElements):
        if (grid[i][j+1] != 0):
            ans = clearNeighbor(grid, i, j+1, numOfLayers, numOfElements)
    else:
        ans = [i, j]
        
    return ans


print(Solution.findFarmland(Solution, [[1,0,0],[0,1,1],[0,1,1]]))