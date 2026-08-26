# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        ans = 0
        
        def dfs(root, maxVal):
            nonlocal ans

            if not root:
                return

            if root.val >= maxVal:
                ans += 1
                maxVal = root.val

            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root, root.val)
        
        return ans
            
            

