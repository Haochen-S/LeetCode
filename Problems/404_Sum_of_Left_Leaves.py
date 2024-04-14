# 404. Sum of Left Leaves

# Done

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum = 0
        
        sum = sumLeftLeaf(root.left, True) + sumLeftLeaf(root.right, False)
        return sum
    
def sumLeftLeaf(root, isLeft):
    if (root == None):
        return 0
    
    sum = 0
    isLeaf = True
    if (root.left != None):
        sum += sumLeftLeaf(root.left, True)
        isLeaf = False
    if (root.right != None):
        sum += sumLeftLeaf(root.right, False)
        isLeaf = False
    
    if (isLeft and isLeaf):
        return root.val + sum
    return sum



