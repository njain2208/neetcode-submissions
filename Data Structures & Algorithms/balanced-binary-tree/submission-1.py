# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        ans = True

        def maxDepth(root):
            nonlocal ans
            if not root:
                return 0 
            left, right = maxDepth(root.left), maxDepth(root.right) 
            if (left >right+1 or left+1 <right):
                ans = False
            return max(left, right)+1
        
        maxDepth(root)

        return ans
        