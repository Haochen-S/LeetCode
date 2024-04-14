# 1848. Minimum Distance to the Target Element

class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        ansIndex = None
        i = 0
        arrayLen = len(nums)
        while (i < arrayLen):
            if (nums[i] == target):
                if (ansIndex == None):
                    ansIndex = i
                    continue
                
                # if (start <= 0):
                #     return abs(ansIndex - start)
                
                if (abs(i - start) < abs(ansIndex - start)):
                    ansIndex = i
 
            i += 1
        return abs(ansIndex - start)
