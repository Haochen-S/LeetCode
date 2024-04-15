# 15. 3Sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # sort the array
        nums.sort()

        # find the ans[]
        ans = []
        lastNum = None
        length = len(nums)
        i = 0

        while (i < length - 2):
            if (lastNum != nums[i] ):
                lastNum = nums[i]
                result = twoSum(nums[i+1:], -lastNum, nums[i])
                if (result != []):
                    ans += result

            i += 1

        return ans
        
# 167. Two Sum II - Input Array Is Sorted
def twoSum(numbers, target, leadNum):
    """
    :type numbers: List[int]
    :type target: int
    :rtype: List[int]
    """
    minIndex = 0
    maxIndex = len(numbers) - 1
    ans = []
    lastNum = None
    while minIndex < maxIndex:
        
        if (lastNum == numbers[minIndex]):
            minIndex += 1
            continue

        if (numbers[minIndex] + numbers[maxIndex] == target):
            ans.append([leadNum, numbers[minIndex], numbers[maxIndex]])
            # next index can not be the same number, avoid duplicate
            lastNum = numbers[minIndex]
            minIndex += 1
        elif (numbers[minIndex] + numbers[maxIndex] > target):
            maxIndex -= 1
        else:
            minIndex += 1

    return ans
