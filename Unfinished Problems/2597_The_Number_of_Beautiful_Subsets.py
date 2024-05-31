# 2597. The Number of Beautiful Subsets
class Solution(object):
    def beautifulSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans = []
        i = 0
        while (i < len(nums)):
            print(nums[i])
            ans.append([nums[i]])
            j = i + 1
            while (j < len(nums)):
                
                if (len(nums[i:j]) != 2):
                    print(nums[i:j])
                    ans.append([nums[i:j]])
                if (abs(nums[i] - nums[j]) != k):
                    print(nums[i], nums[j])
                    ans.append([nums[i], nums[j]])
                j += 1
            i += 1 
        print(ans)
        return len(ans)


#Driver Code
arr = [9,5,7,10,6,2]
n = len(arr)
print(Solution.beautifulSubsets(Solution, arr, 9))

