# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        dictObj = {}

        for i in range(len(inorder)):
            dictObj[inorder[i]] = i

        # leftBorder, rightBorder = float("-inf"), float("inf")
        i = 0
        def dfs(leftBorder, rightBorder):
            nonlocal i
            if i >= len(preorder):
                return None

            if not (leftBorder < dictObj[preorder[i]] < rightBorder):
                i -= 1
                return None

            tempNode = TreeNode(preorder[i])
            tempBoundary = dictObj[preorder[i]]

            i += 1
            tempNode.left = dfs(leftBorder, tempBoundary)
            
            i += 1 
            tempNode.right = dfs(tempBoundary, rightBorder)

            return tempNode

        return dfs(float("-inf"), float("inf"))

        