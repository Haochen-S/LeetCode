# 129. Sum Root to Leaf Numbers

# Done
# RunTime: beats 99.92% user with python -- 15/04/2024
# Memory:  beats 85.73% user with python -- 15/04/2024

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # Done
    # RunTime: beats 99.92% user with python -- 15/04/2024
    # Memory:  beats 85.73% user with python -- 15/04/2024
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return recursive(0, root)

# use recursive to caculate the value
def recursive(num, root):
    if (root.left == None and root.right == None):
        return num * 10 + root.val
    sum = 0
    if (root.left != None):
        sum += recursive(num * 10 + root.val, root.left)
    if (root.right != None):
        sum += recursive(num * 10 + root.val, root.right)
    return sum

