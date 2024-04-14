# 387. First Unique Character in a String
# Done
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """

        first_appearance = {
        }
        number_of_appearance = {
        }
        
        i = 0
        while (i < len(s)):
            if (number_of_appearance.get(s[i]) == None):
                first_appearance[s[i]] = i
                number_of_appearance[s[i]] = 0
            else:
                if (first_appearance.get(s[i]) != None):
                    first_appearance.pop(s[i])
            i += 1

        if (first_appearance == {}):
            return -1
        else:
            return min(first_appearance.values())
# Done
