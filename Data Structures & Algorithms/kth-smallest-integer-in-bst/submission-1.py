# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        i = 1
        ans = root.val
        
        def dfs(root):
            nonlocal i, ans
            if not root:
                return
            dfs(root.left)
            if k == i:
                ans = root.val
                i += 1
                return
            i += 1
            dfs(root.right)
        
        dfs(root)

        return ans   