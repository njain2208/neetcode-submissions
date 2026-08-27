# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def dfs(root, leftBorder, rightBorder):
            if root == None:
                return True
            if not (leftBorder < root.val < rightBorder):
                return False
            return dfs(root.left, leftBorder, root.val) and dfs(root.right, root.val, rightBorder)
        
        return dfs(root, float("-inf"), float("inf"))
        