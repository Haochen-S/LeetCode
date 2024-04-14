# 167. Two Sum II - Input Array Is Sorted

# DONE
import math
class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        minIndex = 0
        maxIndex = len(numbers) - 1

        while minIndex < maxIndex:
            
            if (numbers[minIndex] + numbers[maxIndex] == target):
                return [minIndex + 1, maxIndex + 1]
            elif (numbers[minIndex] + numbers[maxIndex] > target):
                maxIndex -= 1
            else:
                minIndex += 1

        return []


 
 
