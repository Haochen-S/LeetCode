# Done
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        i = 0
        while (i < len(nums)):

            first = nums[i]
            j = i + 1
            while (j < len(nums)):
                if (nums[j] + first == target):
                    aim = []
                    aim.append(i)
                    aim.append(j)
                    return aim

                j += 1

            i += 1
# Done
