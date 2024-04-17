# 623_Add_One_Row_to_Tree.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if (depth == 1):
            return TreeNode(val, root, None)

        depthCounter = 2
        return recursive(root, val, depthCounter, depth)


def recursive(root, val, currDepth, aimDepth):
    if (root == None):
        if (currDepth == aimDepth):
            return TreeNode(val, None, None)
        return None
    
    if (root.left != None):
        if (currDepth < aimDepth):
            root.left = recursive(root.left, val, currDepth + 1, aimDepth)
        elif (currDepth == aimDepth):
            leftRoot = root.left
            root.left = TreeNode(val, leftRoot, None)
    else:
        if (currDepth == aimDepth):
            root.left = TreeNode(val, None, None)

    if (root.right != None):
        if (currDepth < aimDepth):
            root.right = recursive(root.right, val, currDepth + 1, aimDepth)
        elif (currDepth == aimDepth):

            rightRoot = root.right
            root.right = TreeNode(val, None, rightRoot)
    else:
        if (currDepth == aimDepth):
            root.right = TreeNode(val, None, None)

    return root


    # if (root.left != None):
    #     if (currDepth < aimDepth):
    #         root.left = recursive(root.left, val, currDepth + 1, aimDepth)
    #     elif (currDepth == aimDepth):
    #         if (root.left != None):
    #             leftRoot = root.left
    #             root.left = TreeNode(val, leftRoot.left, leftRoot.right)
    #         else:
    #             root.left = TreeNode(val = None)
    #         if (root.right != None):
    #             rightRoot = root.right
    #             root.right = TreeNode(val, rightRoot.left, rightRoot.right)
    #         else:
    #             root.right = TreeNode(val = None)
    
    # if (root.right != None):
    #     if (currDepth < aimDepth):
    #         root.right = recursive(root.right, val, currDepth + 1, aimDepth)
    #     elif (currDepth == aimDepth):
    #         if (root.left != None):
    #             leftRoot = root.left
    #             root.left = TreeNode(val, leftRoot.left, leftRoot.right)
    #         else:
    #             root.left = TreeNode(val = None)
    #         if (root.right != None):
    #             rightRoot = root.right
    #             root.right = TreeNode(val, rightRoot.left, rightRoot.right)
    #         else:
    #             root.right = TreeNode(val = None)
