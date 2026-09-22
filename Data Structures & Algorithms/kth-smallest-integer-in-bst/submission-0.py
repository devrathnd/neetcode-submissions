# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
index = 0
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        global index
        index = 0

        def dfs(node, k):
            if not node:
                return

            #inorder
            result = dfs(node.left, k)
            if result is not None:
                return result

            global index
            index += 1
            if index == k:
                return node.val
            
            result = dfs(node.right, k)
            if result is not None:
                return result
        
        return dfs(root, k)
