# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        ans = []
        queue = collections.deque([root])

        while queue:
            cur = queue.popleft()
            
            if cur == None:
                ans.append("N")
                continue
            
            ans.append(str(cur.val))

            queue.append(cur.left)
            queue.append(cur.right)
        return ",".join(ans)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        listOfNode = collections.deque(data.split(","))

        if not listOfNode:
            return None

        cur = listOfNode.popleft()
        if cur == "N":
            return None

        head = TreeNode(cur)
        queue = collections.deque([head])

        while queue and listOfNode:
            cur = queue.popleft()

            left, right = listOfNode.popleft(), listOfNode.popleft()

            if left != "N":
                cur.left = TreeNode(left)
                queue.append(cur.left)

            if right != "N":
                cur.right = TreeNode(right)
                queue.append(cur.right)
        
        return head

