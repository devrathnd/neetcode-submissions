# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.isGoodNode(root, float('-inf'))

    def isGoodNode(self, node: TreeNode, maxVal: int) -> int:
        if not node:
            return 0
        
        count = 0
        
        #PreOrder DFS
        if node.val >= maxVal:
            count = 1

        newMax = max(maxVal, node.val)
        
        return count + self.isGoodNode(node.left, newMax) + self.isGoodNode(node.right, newMax)