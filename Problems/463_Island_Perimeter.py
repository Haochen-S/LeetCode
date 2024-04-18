# 463. Island Perimeter


class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        numOfLandSurrending = 0
        numOfLayers = len(grid)
        i = 0
        while (i < numOfLayers):
            j = 0
            numOfElements = len(grid[i])
            while (j < numOfElements):
                if (grid[i][j] != 1):
                    j += 1
                    continue

                # if most top and most bot, add one
                if (i == 0):
                    numOfLandSurrending += 1
                if (i == numOfLayers - 1):
                    numOfLandSurrending += 1
                
                # most left or most right, add one
                if (j == 0):
                    numOfLandSurrending += 1
                if (j == numOfElements - 1):
                    numOfLandSurrending += 1
            
                if (j + 1 < numOfElements):
                    if (grid[i][j + 1] != 1):
                        numOfLandSurrending += 1
                if (j - 1 >= 0):
                    if (grid[i][j - 1] != 1):
                        numOfLandSurrending += 1

                if (i + 1 < numOfLayers):
                    if (grid[i + 1][j] != 1):
                        numOfLandSurrending += 1
                if (i - 1 >= 0):
                    if (grid[i - 1][j] != 1):
                        numOfLandSurrending += 1
        
                j += 1

            i += 1

        return numOfLandSurrending


