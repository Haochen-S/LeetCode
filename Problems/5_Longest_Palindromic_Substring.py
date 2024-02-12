# 5. Longest Palindromic Substring
import math

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        ans = ""
        ansSize = 0

        # aabb
        length = len(s)
        checking_length = length
        start = 0
        while (checking_length > 0):
            end = start + checking_length
            while(end <= length):
                solution = Solution()
                if (solution.isPalindromic(s[start:end])):
                    return s[start:end]
                start += 1
                end += 1
            checking_length -= 1
            start = 0
        return ans


    def isPalindromic(self, s):
        length = len(s)
        # even str   a b b a  4/2=2
        #                ^
        if (length % 2 == 0):
            mid1 = int(length / 2)
            mid2 = mid1 - 1
            while (mid2 >= 0):
                if (s[mid1] != s[mid2]):
                    return False
                mid1 += 1
                mid2 -= 1

        # odd str    a b a   3/2=1.5
        #              ^
        else:
            mid = int(math.floor(length / 2))
            front = mid - 1
            back = mid + 1
            while (front >= 0):
                if (s[front] != s[back]):
                    return False
                front -= 1
                back += 1
        return True




print(Solution.longestPalindrome(Solution, "xxadbcbdxxx"))

