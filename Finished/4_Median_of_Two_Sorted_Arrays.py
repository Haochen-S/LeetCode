# 4. Median of Two Sorted Arrays

import math
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1Len = len(nums1)
        nums2Len = len(nums2)
        totalLen = nums1Len + nums2Len

        mergeNum = []
        isEven = False
        if (totalLen % 2 == 0):
            i = totalLen / 2
            isEven = True
        else:
            i = math.floor(totalLen / 2)
        i = int(i)

        counter = 0
        nums1Index = 0
        nums2Index = 0

        while (counter <= i):
            if (nums1Index >= nums1Len):
                mergeNum.append(nums2[nums2Index])
                nums2Index += 1
            elif (nums2Index >= nums2Len):
                mergeNum.append(nums1[nums1Index])
                nums1Index += 1
            elif (nums1[nums1Index] <= nums2[nums2Index]):
                mergeNum.append(nums1[nums1Index])
                nums1Index += 1
            elif (nums1[nums1Index] > nums2[nums2Index]):
                mergeNum.append(nums2[nums2Index])
                nums2Index += 1

            counter += 1
        
        if (isEven):
            return float(mergeNum[i] + mergeNum[i - 1]) / 2

        return mergeNum[i]
    
print(Solution.findMedianSortedArrays(Solution, [1,2], [3,4]))