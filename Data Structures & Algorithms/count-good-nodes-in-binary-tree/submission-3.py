# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

res = 0

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        global res
        res = 0

        self.isGoodNode(root, float('-inf'))

        return res

    def isGoodNode(self, node: TreeNode, maxVal: int):
        if not node:
            return

        #PreOrder DFS
        global res
        if node.val >= maxVal:
            res += 1
        
        self.isGoodNode(node.left, max(maxVal, node.val))
        self.isGoodNode(node.right, max(maxVal, node.val))