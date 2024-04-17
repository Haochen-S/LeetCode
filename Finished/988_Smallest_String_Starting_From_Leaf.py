# 988. Smallest String Starting From Leaf


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import string
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if (root == None):
            return ""

        wordList = recursive(root)

        return findSmallest(wordList)
    
# def convertToString(num):
#     ansStr = ""
#     numStr = str(num)
#     for c in numStr:
#         ansStr += string.ascii_lowercase[int(c)]
#     return ansStr

def findSmallest(wordList):
    smallestWord = wordList[0]
    i = 1
    while (i < len(wordList)):
        if (smallestWord > wordList[i]):
            smallestWord = wordList[i]
        i += 1

    return smallestWord

def recursive(root):
    if (root == None):
        return []
    if (root.left == None and root.right == None):
        return [string.ascii_lowercase[root.val]]
    
    ans = []
    if (root.left != None):
        words = recursive(root.left)
        wordList = []
        for word in words:
            wordList.append(word + string.ascii_lowercase[root.val])
        ans += wordList

    if (root.right != None):
        words = recursive(root.right)
        wordList = []
        for word in words:
            wordList.append(word + string.ascii_lowercase[root.val])
        ans += wordList

    return ans
