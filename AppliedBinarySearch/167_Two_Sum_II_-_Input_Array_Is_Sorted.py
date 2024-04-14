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
        i = 0
        while (i < len(numbers) - 1):
            
            ans = tryFindAns(numbers[i], numbers[i+1:], target)
            if (ans != []):
                return [i + 1, ans + i + 2]
            i += 1

def tryFindAns(num, numbers, target):
    maxIndex = len(numbers) - 1
    minIndex = 0

    while True:
        index = minIndex + (maxIndex - minIndex) // 2

        if (index >= len(numbers)):
            index = len(numbers) - 1

        if (minIndex >= index or maxIndex <= index):
            if (num + numbers[minIndex] == target):
                return minIndex
            if (num + numbers[maxIndex] == target):
                return maxIndex
            if (num + numbers[index] == target):
                return index
            return []
    
        if (num + numbers[index] == target):
            return index
        elif (num + numbers[index] > target):
            maxIndex = index - 1
        else:
            minIndex = index + 1


print(Solution.twoSum(Solution, [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,1,1], 2))


# It returns location of x in given array arr
def binarySearch(num, arr, target):
    l = 0
    r = len(arr)-1

    while l <= r:
        mid = l + (r - l) // 2
        # Check if x is present at mid
        if (arr[mid] + num) == target:
            return mid
 
        # If x is greater, ignore left half
        elif (arr[mid] + num) < target:
            l = mid + 1
 
        # If x is smaller, ignore right half
        else:
            r = mid - 1
 
    # If we reach here, then the element
    # was not present
    return -1
 
 
