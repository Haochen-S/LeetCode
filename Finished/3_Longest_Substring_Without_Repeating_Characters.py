# Done
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (s == ""):
            return 0
        
        index = 0
        answer_list = []

        while (index < len(s)):

            stoped_index = find_non_repeating_part(s, index)
            length = stoped_index - index
            answer_list.append(length)

            index += 1

        greatest = answer_list[0]
        aim_index = 0
        i = 1
        while (i < len(answer_list)):
            if (answer_list[i] > greatest):
                greatest = answer_list[i] 
                aim_index = i
            i += 1

        return greatest

def find_non_repeating_part(s, index):

    char_list = []
    char_list.append(s[index])
    i = index + 1
    while (i < len(s)):
        if (s[i] in char_list):
            return i
        else:
            char_list.append(s[i])

        i += 1
    return i        
# Done
