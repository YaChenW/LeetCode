# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        s = self.getSet(root)
        if len(s) < 2: return -1
        minone = min(s)
        s.remove(minone)
        return min(s)

    def getSet(self, node):
        if node == None: return None
        ret = set([node.val])
        ret1 = self.getSet(node.left)
        ret2 = self.getSet(node.right)
        if ret1 != None: ret = ret | ret1
        if ret2 != None: ret = ret | ret2
        return ret