# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        ans = root

        def recTraversal( root):
            nonlocal ans
            if not root:
                return False
            leftPath, rightPath = recTraversal(root.left), recTraversal(root.right)
            
            if root.val == p.val or root.val == q.val:
                if leftPath or rightPath:
                    ans = root
                return True
            if leftPath and rightPath:
                ans = root
                return True
            return leftPath or rightPath

        recTraversal(root)
        return ans