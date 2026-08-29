# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None

        maxSum = root.val

        def dfs(root):
            nonlocal maxSum
            if not root:
                return 0
            
            leftSum, rightSum = dfs(root.left), dfs(root.right)

            maxSum = max(maxSum, leftSum + rightSum +root.val )
            return max(leftSum + root.val, root.val + rightSum, 0)
        
        dfs(root)
        return maxSum