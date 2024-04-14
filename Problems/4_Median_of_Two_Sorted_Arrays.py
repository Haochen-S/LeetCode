# 4. Median of Two Sorted Arrays

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # middleNumber = 
        isFound = False
        while not isFound:
            
            Solution.findMiddle(nums1)

        
        
        
    def findMiddle(input_list):
        middle = float(len(input_list)) / 2
        if middle % 2 != 0:
            return input_list[int(middle - .5)]
        else:
            return (input_list[int(middle)], input_list[int(middle-1)])
        
        
        
        
        
        
        
        
        
        