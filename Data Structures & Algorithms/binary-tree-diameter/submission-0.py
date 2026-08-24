# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        maxDiameter = 0

        def recursiveTraversal(root):
            nonlocal maxDiameter
            if not root:
                return 0
            
            leftLen, rightLen = recursiveTraversal(root.left),  recursiveTraversal(root.right)
            maxDiameter = max(maxDiameter, leftLen+rightLen)
            
            return max(rightLen,leftLen)+1

        recursiveTraversal(root)
        return maxDiameter  