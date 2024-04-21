# 1971. Find if Path Exists in Graph

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        
        canBeVisited = [False]
        i = 1
        while (i < n):
            canBeVisited.append(False)
            i += 1

        canBeVisited[source] = True
        loop = 0
        while (loop < 6):
            if (canBeVisited[destination]):
                return True
            
            for edge in edges:
                if (canBeVisited[edge[0]] == True):
                    canBeVisited[edge[1]] = True
                if (canBeVisited[edge[1]] == True):
                    canBeVisited[edge[0]] = True
            loop += 1
        if (canBeVisited[destination]):
            return True

        return False
    
print(Solution.validPath(Solution, 10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9))

