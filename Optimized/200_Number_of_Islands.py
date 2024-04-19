# 200. Number of Islands

class Solution(object):

    # find the corner of the island
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        numOfIslands = 0
        numOfLayers = len(grid)
        numOfElements = len(grid[0])
        i = 0
        while (i < numOfLayers):
            j = 0

            while (j < numOfElements):
                left = False
                top = False
                if (grid[i][j] == "0"):
                    j += 1
                    continue
            
                # if most top
                if (i == 0):
                    top = True
                elif (grid[i-1][j] == "0"):
                    top = True
                    
                # most left
                if (j == 0):
                    left = True
                elif (grid[i][j-1] == "0"):
                    left = True

                # check if its the island's corner
                if (left and top):
                    numOfIslands += 1
                    clearNeighbor(grid, i, j, numOfLayers, numOfElements)
                j += 1
            i += 1

        return numOfIslands



def clearNeighbor(grid, i, j, numOfLayers, numOfElements):
    if (grid[i][j] == "0"):
        return
    
    grid[i][j] = "0"

    if (i-1 >= 0):
        clearNeighbor(grid, i-1, j, numOfLayers, numOfElements)
    if (i+1 < numOfLayers):
        clearNeighbor(grid, i+1, j, numOfLayers, numOfElements)

    if (j-1 >= 0):
        clearNeighbor(grid, i, j-1, numOfLayers, numOfElements)
    if (j+1 < numOfElements):
        clearNeighbor(grid, i, j+1, numOfLayers, numOfElements)

    
print(Solution.numIslands(Solution, [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]))
